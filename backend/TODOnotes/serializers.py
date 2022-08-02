from rest_framework.serializers import ModelSerializer
from .models import User
# from .models import Admin


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class AdminModelSerializer(ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = '__all__'
