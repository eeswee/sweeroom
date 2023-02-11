from django.forms import ModelForm
from .models import Vendor,Item
from django import forms

class ItemFormAdmin(ModelForm):
	class Meta:
		model = Item
		fields = ('name','code', 'price','moq','lead_time','design_size','material', 'vendor', 'client', 'assistant')
		labels = {
			'name': 'Item Name',
			'code': 'code',
			'price': 'price',
			'moq': 'moq',
			'lead_time': 'lead time',
			'design_size': 'design_size',
			'material': 'material',
			'vendor': 'vendor',
			'client': 'client',
			'assistant': 'assistant',
		}
		
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'item Name'}),
			'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'item code'}),
			'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'price'}),
			'moq': forms.TextInput(attrs={'class':'form-control', 'placeholder':'moq'}),
			'lead_tiem': forms.TextInput(attrs={'class':'form-control', 'placeholder':'lead time'}),
			'design_size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'box size : width x depth x height'}),
			'material': forms.Textarea(attrs={'class':'form-control', 'placeholder':'material'}),
			'vendor': forms.Select(attrs={'class':'form-select', 'placeholder':'vendor'}),
			'client': forms.Select(attrs={'class':'form-select', 'placeholder':'client'}),
			'assistant': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Assistant'}),
        }

# User item Form
class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ('name','code', 'price','moq','lead_time','design_size','material', 'vendor', 'client', 'assistant')
		labels = {
			'name': 'Item name',
			'code': 'code',
			'price': 'price',
			'moq': 'moq',
			'lead_time': 'lead time',
			'design_size': 'design_size',
			'material': 'material',
			'vendor': 'vendor',
			'client': 'client',
			'assistant': 'assistant',
		}
		
			


		widgets = {
			
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Item Name'}),
			'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'item code'}),
			'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'price'}),
			'moq': forms.TextInput(attrs={'class':'form-control', 'placeholder':'moq'}),
			'lead_tiem': forms.TextInput(attrs={'class':'form-control', 'placeholder':'lead time'}),
			'design_size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'box size : width x depth x height'}),
			'material': forms.Textarea(attrs={'class':'form-control', 'placeholder':'material'}),
			'vendor': forms.Select(attrs={'class':'form-select', 'placeholder':'vendor'}),
			'client': forms.Select(attrs={'class':'form-select', 'placeholder':'client'}),
			'assistant': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Assistant'}),
			
    	}









class VendorForm(ModelForm):
	class Meta:
		model = Vendor
		fields = ('name', 'owner', 'owner_phone', 'address','zip_code', 'web','manager_name', 'manager_phone','manager_email', 'assistant')
		labels = {
			'name': 'Vendor Name',
			'owner': 'Vendor Owner',
			'owner_phone': 'Owner Phone',
			'address': 'Company Address',
			'zip_code': 'Zip Code',
			'web': 'Vendor Website',
			'manager_name': 'Manager name',
			'manager_phone': 'Manager Phone',			
			'manager_email': 'Manager Email',			
			'assistant': 'Assitant Name',						
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vendor Name'}),
			'owner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vendor Owner'}),
			'owner_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Owner Phone'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vendor Website'}),
			'manger_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager Name'}),
			'manager_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager Phone'}),
			'manager_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Manager Email'}),
			'assistant': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Assistant'}),
		}
		


     