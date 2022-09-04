from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TODOnotes.views import UserModelViewSet, ProjectModelViewSet, ToDoModelViewSet

app_name = 'TODOnotes'

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]