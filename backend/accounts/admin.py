from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import EmailVerificationToken, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "student_or_staff_id", "role", "is_email_verified", "is_active")
    list_filter = ("role", "is_email_verified", "is_active", "is_staff")
    search_fields = ("email", "student_or_staff_id", "first_name", "last_name")

    fieldsets = (
        (None, {"fields": ("email", "student_or_staff_id", "password")}),
        ("ชื่อ", {"fields": ("first_name", "last_name", "first_name_en", "last_name_en")}),
        (
            "สิทธิ์",
            {
                "fields": (
                    "role",
                    "is_active",
                    "is_email_verified",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("อื่น ๆ", {"fields": ("avatar_url", "created_by", "last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "student_or_staff_id", "role", "password1", "password2"),
            },
        ),
    )


@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "purpose", "expires_at", "used_at")
    list_filter = ("purpose",)
    search_fields = ("user__email", "token")
