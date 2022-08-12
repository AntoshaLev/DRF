import io

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import User, Project, ToDo
from .serializers import UserModelSerializer, UserSerializer, ProjectModelSerializer, ToDoModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


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
