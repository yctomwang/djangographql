from django.core.management.base import BaseCommand
from people.models import Person, Address

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        address = Address.objects.create(number=123, street="Main St", city="New York", state="NY")
        Person.objects.create(email="johndoe@example.com", name="John Doe", address=address)
        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))
