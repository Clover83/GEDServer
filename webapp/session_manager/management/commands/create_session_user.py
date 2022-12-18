from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a user for /profile/'

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("password", type=str, help="Password of the user")

    def handle(self, *args, **kwargs):
        uname = kwargs["username"]
        passw = kwargs["password"]
        User.objects.create_user(uname, password=passw)
