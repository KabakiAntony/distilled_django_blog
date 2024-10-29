from django.contrib import admin
from .models import Blogs  # Import your blog model

class DistilledDjangoBlogAdminSite(admin.AdminSite):
	site_header = "Distilled Django Blog Admin"
	site_title = "Distilled Django"
	index_title = "Welcome to Distilled Django Blog Admin"

# Register your model with the custom admin site
admin_site = DistilledDjangoBlogAdminSite(name='custom_admin')
admin_site.register(Blogs)  # Register your blog model here
