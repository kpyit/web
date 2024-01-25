from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')





