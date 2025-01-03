from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)  # User model을 control할거임
class CustomUserAdmin(UserAdmin):  # UserModel 상속/ 그냥 admin 패널보다 기능많음
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "language",
                    "currency",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),  # hidden
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "name",
        "is_host",
    )  # 뭐가 보일지 결정 +model에 있는것들이여야함
