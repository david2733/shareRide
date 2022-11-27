"""Users models admin."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project_data.users.models import Profile, User

# from django.utils.translation import gettext_lazy as _

# from project_data.users.forms import UserAdminChangeForm, UserAdminCreationForm


class CustomUserAdmin(UserAdmin):
    """User model admin."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""
    list_display = ('user', 'reputation', 'rides_taken', 'rides_offered')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('reputation', )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
