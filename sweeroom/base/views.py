from django.shortcuts import redirect, render, get_object_or_404
from .models import User,Item,Vendor

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import VendorForm,ItemForm,ItemFormAdmin

import csv
from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


from django.core.paginator import Paginator
# Create your views here.


def vendor_items(request, vendor_id):
	# Grab the vendor
	vendor = Vendor.objects.get(id=vendor_id)	
	# Grab the items from that vendor
	items = vendor.item_set.all()
	if items:
		return render(request, 'base/vendor_items.html', {
			"items":items
			})
	else:
		messages.success(request, ("That vendor Has No items At This Time..."))
		return redirect('admin_approval')


# Create Admin item Approval Page
def admin_approval(request):
	# Get The vendors
	vendor_list = Vendor.objects.all()
	# Get Counts
	item_count = Item.objects.all().count()
	vendor_count = Vendor.objects.all().count()
	user_count = User.objects.all().count()

	item_list = Item.objects.all()
	if request.user.is_superuser:
		if request.method == "POST":
			# Get list of checked box id's
			id_list = request.POST.getlist('boxes')

			# Uncheck all items
			item_list.update(approved=False)

			# Update the database
			for x in id_list:
				Item.objects.filter(pk=int(x)).update(approved=True)
			
			# Show Success Message and Redirect
			messages.success(request, ("item List Approval Has Been Updated!"))
			return redirect('list-items')



		else:
			return render(request, 'base/admin_approval.html',
				{"item_list": item_list,
				"item_count":item_count,
				"vendor_count":vendor_count,
				"user_count":user_count,
				"vendor_list":vendor_list})
	else:
		messages.success(request, ("You aren't authorized to view this page!"))
		return redirect('home')


	return render(request, 'items/admin_approval.html')

def my_items(request):
	if request.user.is_authenticated:
		me = request.user.id
		items = Item.objects.filter(vendor=me)
		return render(request, 
			'base/my_items.html', {
				"items":items
			})

	else:
		messages.success(request, ("You Aren't Authorized To View This Page"))
		return redirect('home')





def vendor_pdf(request):
	# Create Bytestream buffer
	buf = io.BytesIO()
	# Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	# Add some lines of text
	#lines = [
	#	"This is line 1",
	#	"This is line 2",
	#	"This is line 3",
	#]
	
	# Designate The Model
	vendors = Vendor.objects.all()

	# Create blank list
	lines = []

	for vendor in vendors:
		lines.append(vendor.name)
		lines.append(vendor.address)
		lines.append(vendor.zip_code)
		lines.append(vendor.web)
		lines.append(vendor.manager_name)
		lines.append(vendor.manager_phone)
		lines.append(vendor.manager_email)
		lines.append(vendor.assistant)
		lines.append(" ")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='vendor.pdf')

# Generate CSV File vendor List
def vendor_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=vendors.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	vendors = Vendor.objects.all()

	# Add column headings to the csv file
	writer.writerow(['vendor Name', 'Address', 'Zip Code', 'Web', 'Manager Name','Manager Phone''Manager email', 'Assistant'])

	# Loop Thu and output
	for vendor in vendors:
		writer.writerow([vendor.name, vendor.address, vendor.zip_code, vendor.web, vendor.manage_name,vendor.manage_phone,vendor.manage_email,vendor.assistant ])

	return response


def vendor_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=vendors.txt'
	# Designate The Model
	vendors = Vendor.objects.all()

	# Create blank list
	lines = []
	# Loop Thu and output
	for vendor in vendors:
		lines.append(f'{vendor.name}\n{vendor.address}\n{vendor.manager_name}\n{vendor.manager_email}\n{vendor.web}\n{vendor.assistant}\n\n\n')

	#lines = ["This is line 1\n", 
	#"This is line 2\n",
	#"This is line 3\n\n",
	#"John Elder Is Awesome!\n"]

	# Write To TextFile
	response.writelines(lines)
	return response

def delete_vendor(request, vendor_id):
	vendor = Vendor.objects.get(pk=vendor_id)
	vendor.delete()
	return redirect('list-vendors')		



def update_vendor(request, vendor_id):
	vendor = vendor.objects.get(pk=vendor_id)
	form = VendorForm(request.POST or None, request.FILES or None, instance=vendor)
	if form.is_valid():
		form.save()
		return redirect('list-vendors')

	return render(request, 'base/update_vendor.html', 
		{'vendor': vendor,
		'form':form})


def search_vendors(request):
	if request.method == "POST":
		searched = request.POST['searched']
		vendors = Vendor.objects.filter(name__contains=searched)
	
		return render(request, 
		'base/search_vendors.html', 
		{'searched':searched,
		'vendors':vendors})
	else:
		return render(request, 
		'base/search_vendors.html', 
		{})



def show_vendor(request, vendor_id):
	vendor = Vendor.objects.get(pk=vendor_id)
	# vendor_owner = User.objects.get(pk=vendor.owner)

	# Grab the items from that vendor
	items = vendor.item_set.all()

	return render(request, 'base/show_vendor.html', 
		{'vendor': vendor,
		# 'vendor_owner':vendor_owner,
		'items':items})


def list_vendors(request):
	#vendor_list = vendor.objects.all().order_by('?')
	vendor_list = Vendor.objects.all()

	# Set up Pagination
	p = Paginator(Vendor.objects.all(), 3)
	page = request.GET.get('page')
	vendors = p.get_page(page)
	nums = "a" * vendors.paginator.num_pages
	return render(request, 'base/vendor.html', 
		{'vendor_list': vendor_list,
		'vendors': vendors,
		'nums':nums}
		)
def add_vendor(request):
	submitted = False
	if request.method == "POST":
		form = VendorForm(request.POST, request.FILES)
		if form.is_valid():
			vendor = form.save(commit=False)
			vendor.owner = request.user.id # logged in user
			vendor.save()
			#form.save()
			return 	HttpResponseRedirect('/add_vendor?submitted=True')	
	else:
		form = VendorForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'base/add_vendor.html', {'form':form, 'submitted':submitted})

def search_items(request):
	if request.method == "POST":
		searched = request.POST['searched']
		items = Item.objects.filter(description__contains=searched)
	
		return render(request, 
		'base/search_items.html', 
		{'searched':searched,
		'items':items})
	else:
		return render(request, 
		'base/search_items.html', 
		{})




def show_item(request, item_id):
	item = Item.objects.get(pk=item_id)
	return render(request, 'base/show_item.html', {
			"item":item
			})


def delete_item(request, item_id):
	item = Item.objects.get(pk=item_id)
	if request.user == item.manager:
		item.delete()
		messages.success(request, ("item Deleted!!"))
		return redirect('list-items')		
	else:
		messages.success(request, ("You Aren't Authorized To Delete This item!"))
		return redirect('list-items')		

def add_item(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = ItemFormAdmin(request.POST)
			if form.is_valid():
					form.save()
					return 	HttpResponseRedirect('/add_item?submitted=True')	
		else:
			form = ItemForm(request.POST)
			if form.is_valid():
				#form.save()
				item = form.save(commit=False)
				item.assistant = request.user # logged in user
				item.save()
				return 	HttpResponseRedirect('/add_item?submitted=True')	
	else:
		# Just Going To The Page, Not Submitting 
		if request.user.is_superuser:
			form = ItemFormAdmin
		else:
			form = ItemForm

		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'base/add_item.html', {'form':form, 'submitted':submitted})





def update_item(request, item_id):
	item = Item.objects.get(pk=item_id)
	if request.user.is_superuser:
		form = ItemFormAdmin(request.POST or None, instance=item)	
	else:
		form = ItemForm(request.POST or None, instance=item)
	
	if form.is_valid():
		form.save()
		return redirect('list-items')

	return render(request, 'base/update_item.html', 
		{'item':item,
		'form':form})





def all_items(request):
	item_list = Item.objects.all().order_by('name')
	return render(request, 'base/item_list.html', 
		{'item_list': item_list})


def home (request):
    
    return render(request,'base/home.html')



# .order_by('name')