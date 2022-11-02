from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from project_data.utils.models import CRideModel

# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _


class User(CRideModel, AbstractUser):
    """
    User model

    extend from Django's Abstract User, change the username field to email and add some extra fields.
    """

    email = models.EmailField(
        "email addres",
        unique=True,
        error_messages={
            "unique": "A user with that email already exists",
        },
    )
    phone_regex = RegexValidator(
        regex=r"\+?1?\d{9,15}$",
        message="Phone number must be enetered in the format: +000000000. up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    is_client = models.BooleanField(
        "client status",
        default=True,
        help_text=(
            "Help easily distinguish users and perform queries",
            "Clients are the main type of users.",
        ),
    )
    is_verified = models.BooleanField(
        "verified",
        default=False,
        help_text="Set to true when the user have verified its email address.",
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

    # def get_absolute_url(self):
    #     """Get url for user's detail view.

    #     Returns:
    #         str: URL for user detail.

    #     """
    #     return reverse("users:detail", kwargs={"username": self.username})
