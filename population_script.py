import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','readler.settings')
import django
import datetime
import pytz
django.setup()
from readler.backendAPI.models import *
from django.contrib.auth import get_user_model
from django.utils import timezone
timezone.now()

CustomUser = get_user_model()
def populate():
  print("ello")

if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script finished successfully')