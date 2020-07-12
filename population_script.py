import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','readler.settings')
import django
import datetime
import pytz
from decouple import config
django.setup()
from readler.backendAPI.models import *
from django.contrib.auth import get_user_model
from django.utils import timezone
timezone.now()
CustomUser = get_user_model()

def createSuperUser():
  super_email = config('DJANGO_SUPER_USER_EMAIL', default='')
  super_pass = config('DJANGO_SUPER_USER_PASSWORD', default='')
  CustomUser.objects.filter(email=super_email).delete()
  CustomUser.objects.create_superuser(super_email,super_pass)

def populate():
    createSuperUser()
    users = [
        {
            "firstName": "Mason",
            "lastName": "Parkin",
            "email": "MasonParkin@armyspy.com",
            "password": "aeKai5OHeiph",
            "middleNames": "Cooper"
        },
        {
            "firstName": "Daniel",
            "lastName": "Schofield",
            "email": "DanielSchofield@jourrapide.com",
            "password": "UeK7wiehi",
        },
        {
            "firstName": "Adam",
            "lastName": "Goddard",
            "email": "AdamGoddard@teleworm.us",
            "password": "eixei4Roh",
        },
        {
            "firstName": "Bethany",
            "lastName": "Hunt",
            "email": "BethanyHunt@teleworm.us",
            "password": "mohje0Ahti3",
        },
    ]

    # Init users
    for u in users:
        user = CustomUser.objects.get_or_create(
            email=u['email'], first_name=u['firstName'], last_name=u['lastName'])[0]
        if 'middleNames' in u:
            user.middleNames = u['middleNames']
        if 'username' in u:
            user.username = u['username']
        user.set_password(u['password'])
        user.save()
    USER_MASON = CustomUser.objects.get(email=users[0]['email'])
    USER_DAN = CustomUser.objects.get(email=users[1]['email'])
    USER_ADAM = CustomUser.objects.get(email=users[2]['email'])
    USER_BETHANY = CustomUser.objects.get(email=users[3]['email'])

    settings = [
        {
            'user': USER_MASON,
            'fontFamily': 'Helvetica New',
            'fontSize': '24px',
            'lineHeight': '18px',
        },
        {
            'user': USER_DAN,
            'fontFamily': 'Calibri Old',
            'parMargin': '1.5em',
            'fontSize': '24px',
            'lineHeight': '18px',
        },
        {
            'user': USER_ADAM,
            'fontFamily': 'Unavailable font',
            'parMargin': '1em',
            'fontSize': '12px',
        },
        {
            'user': USER_BETHANY,
            'parMargin': '1.5em',
            'lineHeight': '18px',
        },
    ]
    # Init settings
    for s in settings:
        setting = Settings.objects.get_or_create(user=s['user'])[0]
        if 'fontFamily' in s:
            setting.fontFamily = s['fontFamily']
        if 'fontSize' in s:
            setting.fontSize = s['fontSize']
        if 'parMargin' in s:
            setting.parMargin = s['parMargin']
        if 'lineHeight' in s:
            setting.lineHeight = s['lineHeight']
        setting.save()


if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script finished successfully')
