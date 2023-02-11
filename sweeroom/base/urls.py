from django.urls import path
from base import views


urlpatterns = [
    path('',views.home,name="home"),
    path('items', views.all_items, name="list-items"),
    path('update_item/<item_id>', views.update_item, name='update-item'),		
    path('add_item', views.add_item, name='add-item'),
	path('delete_item/<item_id>', views.delete_item, name='delete-item'),
    path('show_item/<item_id>', views.show_item, name='show-item'),
    path('search_items', views.search_items, name='search_items'),
    path('my_items', views.my_items, name='my_items'),

    path('list_vendor', views.list_vendors, name='list-vendors'),
    path('add_vendor', views.add_vendor, name='add-vendor'),
    path('show_vendor/<vendor_id>', views.show_vendor, name='show-vendor'),	
	path('search_vendors', views.search_vendors, name='search-vendors'),
	path('update_vendor/<vendor_id>', views.update_vendor, name='update-vendor'),
	path('delete_vendor/<vendor_id>', views.delete_vendor, name='delete-vendor'),
    path('vendor_text', views.vendor_text, name='vendor_text'),
	path('vendor_csv', views.vendor_csv, name='vendor_csv'),
	path('vendor_pdf', views.vendor_pdf, name='vendor_pdf'),

    path('vendor_items/<vendor_id>', views.vendor_items, name='vendor-items'),
	path('admin_approval', views.admin_approval, name='admin_approval'),
]
