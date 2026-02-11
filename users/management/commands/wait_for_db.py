# Step 1: Import core requirements
import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from MySQLdb import OperationalError as MySQLOpError 

class Command(BaseCommand): # Step 2: Define Command Class
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options): # Step 3: Define Handle Method
        self.stdout.write('Waiting for database...')
        db_up = False
        
        while db_up is False: # Step 4: The Retry Loop
            try:
                # Step 5: Connectivity Check (Zero-Inference Reliability)
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, MySQLOpError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        # Step 6: Success Logging
        self.stdout.write(self.style.SUCCESS('Database available!'))