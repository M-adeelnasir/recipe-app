from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError

class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError,OperationalError):
                self.stdout.write('Database unavailaible, waiting for 1 sec ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is availaible!'))        