from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.accounts import forms as accounts_form
from apps.accounts import models as accounts_models


class UserAdmin(BaseUserAdmin):
    # Forms for add and update users
    form = accounts_form.UserChangeForm
    add_form = accounts_form.UserCreationForm

    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_admin",
    ]
    list_editable = ["is_active", "is_staff", "is_admin"]
    list_filter = ["is_active", "is_staff", "is_admin"]
    fieldsets = [
        (
            None,
            {"fields": [("username", "slug"), "password"]},
        ),
        (
            "Personal info",
            {
                "fields": [
                    ("first_name", "last_name"),
                    "email",
                    "phone_number",
                    "image",
                ]
            },
        ),
        ("Permissions", {"fields": [("is_active", "is_staff", "is_admin")]}),
    ]
    prepopulated_fields = {"slug": ["username"]}

    search_fields = ["username", "email", "phone_number"]
    ordering = ["id"]
    filter_horizontal = []


admin.site.register(accounts_models.User, UserAdmin)
admin.site.unregister(Group)
