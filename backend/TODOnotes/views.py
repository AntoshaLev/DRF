from rest_framework.viewsets import ModelViewSet
from .models import User
# from .models import Admin
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


# class AdminModelViewSet(ModelViewSet):
#     serializer_class = UserModelSerializer
#     queryset = Admin.objects.all()


