from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import TestForm, UserInfoForm, DiaryRecordForm
from emotion_diary.models import User, UserInfo
def base(request):
    return HttpResponse('diary')

class UsersView(View):
    def get(self, request, *args,):
        users = User.objects.all()
        return render(request, 'users.html', context={'users': users})

class TestView(View):
    def get(self, request, *args, **kwargs):
        form = TestForm()
        return render(request, 'test.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = TestForm(request.POST)
        if form.is_valid():
            new_user = User(
                id = form.cleaned_data['id'],
                username = form.cleaned_data['username'])
            new_user.save()

class UserInfoView(View):
    def get(self,request, *args, **kwargs):
        form = UserInfoForm
        return render(request, 'info.html', {'form':form})
    def post(self,request, *args, **kwargs):
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('success')

class AddedInfo(View):
    model = UserInfo

'''''
class CreateRecord(View):
    def get(self, request, *args, **kwargs):
        form = UserInfoForm
        return render(request, 'from_example.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        return HttpResponse('error')
'''

class CreateRecord(View):
    def get(self, request, *args, **kwargs):
        form = DiaryRecordForm
        return render(request, 'new_diary.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = DiaryRecordForm(request.POST)
        if form.is_valid():
            situation = form.cleaned_data['situation']
            emotions = form.cleaned_data['emotions']

        return HttpResponse(form)



