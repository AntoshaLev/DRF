# from django.db import models
# from TODOnotes.models import User
#
#
# class Project(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     repo = models.URLField(blank=True)
#     users = models.ManyToManyField(User)
#
#     def __str__(self):
#         return self.name
#
#
# class ToDo(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     text = models.TextField()
#     creation_date = models.DateTimeField(auto_now_add=True)
#     update_date = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f'{self.project} {self.user} {self.text}'
