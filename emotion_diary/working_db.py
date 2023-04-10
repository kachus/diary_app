from django.db import models
from emotion_diary.models import User, UserInfo


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")

import django
django.setup()

from django.core.management import call_command

new_user = User(id = '9878904', username = 'test2')
