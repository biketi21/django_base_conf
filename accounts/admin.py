from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "firstname",
        "last_login",
        "is_active",
        "is_staff",
    )
    search_fields = ("email", "firstname")
    readonly_fields = ("date_joined", "last_login")

    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ("is_staff", "is_superuser")
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

