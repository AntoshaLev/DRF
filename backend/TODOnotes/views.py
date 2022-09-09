import io

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from .models import User, Project, ToDo
from .serializers import UserModelSerializer, UserSerializer, ProjectModelSerializer, ToDoModelSerializer, \
    UserModelSerializerV2, ProjectSerializer


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self):
        # UserModelSerializerV2
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer


class ProjectModelViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    # pagination_class = ProjectsLimitOffsetPagination
    # DjangoFilterBackend - фильтрация в url /?field=значение
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    # pagination_class = ToDoLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['text', 'is_active']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.is_active = False
            instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def user_api_get(request, pk=None):
    if pk is not None:
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user)
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def user_get(request, pk=None):
    if pk is not None:
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user)
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def user_post(request, pk=None):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = UserSerializer(data=json_data)
    elif request.method == 'PUT':
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=json_data)
    elif request.method == 'PATCH':
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=json_data, partial=True)

    if serializer.is_valid():
        user = serializer.save()
        serializer = UserSerializer(user)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def project_api_get(request):
    books = Project.objects.all()
    serializer = ProjectSerializer(books, many=True)
    return Response(serializer.data)


def project_get(request):
    books = Project.objects.all()
    serializer = ProjectSerializer(books, many=True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)