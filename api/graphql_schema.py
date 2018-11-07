from graphene_django import DjangoObjectType
import graphene
from api.models import WobblyUser


class User(DjangoObjectType):
    class Meta:
        model = WobblyUser

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return WobblyUser.objects.all()

schema = graphene.Schema(query=Query)