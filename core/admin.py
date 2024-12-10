from django.contrib import admin
from .models import Profile

# Register your models here.

#this decorator is another form to register de model in the admin 
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','photo']
    raw_id_fields = ['user']

# admin.site.register(ProfileAdmin)