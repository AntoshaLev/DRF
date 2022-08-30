from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TODOnotes.views import UserModelViewSet, ProjectModelViewSet, ToDoModelViewSet, user_post, user_get, UserApiView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', obtain_auth_token),
    path('user_post', user_post),
    path('user_post/<int:pk>', user_post),
    path('user_get', user_get),
    path('user_api_get', user_get),
    path('user_api_get_class', UserApiView.as_view()),
    path('user_get/<int:pk>', user_get),
]
