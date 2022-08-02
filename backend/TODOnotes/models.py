from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _


# class User(models.Model):
#     user_name = models.CharField(max_length=64)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.CharField(max_length=64, unique=True)
#
#
# class Admin(models.Model):
#     admin_name = models.CharField(max_length=64)
#     admin_email = models.CharField(max_length=64, unique=True)

class User(models.Model):
    user_name = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. ASCII letters and digits only.")
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.CharField(
        _("email address"),
        max_length=256,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists.")
        }
    )
