from django.core.management.base import BaseCommand 
from myapp.models import User 

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        user = User(name='John', email='joht@mail.ru', password='secret', age=25)
        # ...
        user.save()
        self.stdout.write(f'{user}')#тут вызов __str__

