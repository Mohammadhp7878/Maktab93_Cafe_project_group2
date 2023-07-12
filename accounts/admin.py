from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'role')
    list_filter = ()
    ordering = ('role','first_name')
    filter_horizontal = ()
    fieldsets = (
        ('Contact Info', {'fields': ('phone_number', 'email')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'role')}),
        ('password', {'fields':('password',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )


admin.site.register(models.User, CustomUserAdmin)