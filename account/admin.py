from django.contrib import admin
from django.contrib.auth import get_user_model  #allows access to our custom user model
from django.contrib.auth.admin import UserAdmin #allows inheritance of UserAdmin class to override some functionalities
from django.utils.translation import gettext_lazy as _
from .models import Team, Player, Fan, Vendor
# Register your models here.

'''
Create your custom admin model to match the 
custom user model created (no email)
'''

class MyUserAdmin(UserAdmin):
    #set the fieldsets for a user
    '''
    the fieldset is a tuple of tuples. each tuple has two items
    1. a string
    2. s dictionary (key amd tuple of values)
    '''

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    #set the fieldsets to add a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

    #set the view on the admin site
    list_display = ('email', 'is_staff', 'is_active', 'is_team', 'is_player', 'is_fan')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name')
    ordering = ('-date_joined',)

#register your custom user manager and custom user admin
admin.site.register(get_user_model(), MyUserAdmin)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Fan)
admin.site.register(Vendor)
