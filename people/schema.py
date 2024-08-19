import graphene
from graphene_django import DjangoObjectType
from .models import Person, Address  # Ensure these imports are correct

class AddressType(DjangoObjectType):
    class Meta:
        model = Address

class PersonType(DjangoObjectType):
    class Meta:
        model = Person

class Query(graphene.ObjectType):
    people = graphene.List(PersonType)

    def resolve_people(self, info):
        return Person.objects.all()

schema = graphene.Schema(query=Query)  # Ensure this line is present
