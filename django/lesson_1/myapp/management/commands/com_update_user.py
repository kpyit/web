from django.core.management.base import BaseCommand 
from myapp.models import User 

class Command(BaseCommand):
    help = "Get user with age greater <age>"

    def add_argumetns(self, parser):
        parser.add_argument('age', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name # обновление имени  нет проверки правда
        user.save()
        self.stdout.write(f'{user}')# тут вызов __str__