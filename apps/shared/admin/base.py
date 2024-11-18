from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin

admin.site.unregister(Group)


# admin.site.unregister(User)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_vertical = ("permissions",)

# @admin.register(User)
# class UserAdmin(BaseUserAdmin, ModelAdmin):
#     change_password_form = AdminPasswordChangeForm
#     add_form = UserCreationForm
#     form = UserChangeForm
#     list_display = ("username", "email", "is_active", "is_staff", "is_superuser")
#     list_filter = ("is_active", "is_staff", "is_superuser")
#     search_fields = ("username", "email")
#     ordering = ("username",)
#     list_editable = ("is_active", "is_staff", "is_superuser")
#     filter_vertical = ("groups", "user_permissions")
