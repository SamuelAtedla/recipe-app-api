""" django command to wait for the db to be available"""
from django.core.management import BaseCommand


class Command(BaseCommand):
    """django command to wait for database"""

    def handle(self, *args, **options):
        pass
