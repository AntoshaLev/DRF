from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


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


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    repo = models.URLField(blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project} {self.user} {self.text}'

    def delete(self, using=None, keep_parents=False):
        current_todo = self.is_active = False
        return current_todo
