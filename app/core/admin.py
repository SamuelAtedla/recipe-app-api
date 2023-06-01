""" Django admin customization"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# for language translation
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """define the admin pages for users."""
    ordering = ["id"]
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        )
    )


admin.site.register(models.User, UserAdmin)
