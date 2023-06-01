""" django command to wait for the db to be available"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """django command to wait for database"""

    def handle(self, *args, **options):
        """ handles checking of database up """

        self.stdout.write('waiting for database to start ...')
        db_up = False
        trial_count=0;
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                if trial_count>8 :
                    break
                self.stdout.write(
                    'database unavilable, wait for 1 second...')
                time.sleep(1)
                trial_count+=1
        self.stdout.write(self.style.SUCCESS('Database available'))
