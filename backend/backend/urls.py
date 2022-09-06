from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from TODOnotes.views import user_post, user_get, UserApiView, project_get
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title='ToDo List',
        default_version='1.0',
        description='Some todo list',
        contact=openapi.Contact(email='test@mail.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_get', project_get),
    path('api/', include('TODOnotes.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', obtain_auth_token),
    path('user_post', user_post),
    path('user_post/<int:pk>', user_post),
    path('user_get', user_get),
    path('user_api_get', user_get),
    path('user_api_get_class', UserApiView.as_view()),
    path('user_get/<int:pk>', user_get),
    path('swagger/', schema_view.with_ui()),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]
