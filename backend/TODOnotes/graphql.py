import graphene
from graphene_django import DjangoObjectType

from .models import User, Project, ToDo


class TODOType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserObjectType)

    all_info_for_user = graphene.Field(UserObjectType, id=graphene.Int(required=True))

    def resolve_all_info_for_user(root, info):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

    def resolve_all_users(self, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectObjectType)

    def resolve_all_project(self, info):
        return Project.objects.all()

    all_todos = graphene.List(ProjectObjectType)

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    get_user_by_id = graphene.Field(UserObjectType, pk=graphene.Int(required=True))

    def resolve_get_user_by_id(self, info, pk):
        return User.objects.get(pk=pk)

    get_user_by_name = graphene.List(UserObjectType,
                                     first_name=graphene.String(required=False),
                                     last_name=graphene.String(required=False)
                                     )

    def resolve_get_user_by_name(self, info, first_name=None, last_name=None):
        if not first_name and not last_name:
            return User.objects.all()
        params = {}
        if first_name:
            params['first_name__contains'] = first_name
        if last_name:
            params['last_name__contains'] = last_name
        return User.objects.filter(**params)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()
        return cls(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.Int(required=False)

    user = graphene.Field(UserObjectType)

    @classmethod
    def mutate(cls, root, info, pk, user_name=None, first_name=None, last_name=None, email=None):
        user = User.objects.get(pk=pk)
        if user_name:
            user.user_name = user_name
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.birthday_year = email

        if user_name or first_name or last_name or email:
            user.save()
        return cls(user)


class Mutations(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
