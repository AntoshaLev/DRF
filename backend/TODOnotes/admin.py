from django.contrib import admin
from .models import User, Project, ToDo

admin.site.register(User)
admin.site.register(Project)
admin.site.register(ToDo)
