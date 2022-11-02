from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# from django.utils.translation import gettext_lazy as _

# from project_data.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


admin.site.unregister(User)
admin.site.register(User)
