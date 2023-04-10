from django.shortcuts import render
from django.views import View

from emotion_diary.models import User, UserInfo

def index(request):
    return render(request, 'main.html', context={'who': 'diary'})

