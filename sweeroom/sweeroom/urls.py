from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("base.urls")),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure Admin Titles
admin.site.site_header = "EeesRoom Administration Page"
admin.site.site_title = "members title"
admin.site.index_title = "Welcome To The Addmin Area..."