# from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
# from TODOnotes.serializers import UserModelSerializer
# from .models import Project, ToDo
#
#
# class ProjectModelSerializer(ModelSerializer):
#     # users = UserModelSerializer(many=True)
#     users = StringRelatedField(many=True)
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class ToDoModelSerializer(HyperlinkedModelSerializer):
#     user = UserModelSerializer()
#     # user = StringRelatedField()
#     project = ProjectModelSerializer()
#
#     class Meta:
#         model = ToDo
#         fields = '__all__'
