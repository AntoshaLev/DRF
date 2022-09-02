from rest_framework.exceptions import ValidationError
from rest_framework.fields import URLField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField, Serializer, \
    CharField
from .models import User, ToDo, Project


class UserSerializer(Serializer):
    user_name = CharField(max_length=150)
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    email = CharField(max_length=256)

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

    #   def validate_birthday_year(self, value):
    #       if value > 2004:
    #           raise ValidationError('18+')

    def validate(self, attrs):
        if attrs.get('first_name') == 'Anna' and attrs.get('last_name') == 'Lev':
            raise ValidationError('Вы не Анна!')
        return attrs


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelSerializerV2(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
        ]


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    # user = UserModelSerializer()
    # project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
