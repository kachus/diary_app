from django import forms
from django.forms import ModelForm
from .models import UserInfo


class TestForm(forms.Form):
    id = forms.CharField(label='id')
    username = forms.CharField(label='Username')


class UserInfoForm(ModelForm):
    required_css_class = 'required-filed'

    situation = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",
                                                              "placeholder":'Опишите ситуацию',
                                                              "rows":3}))
    thoughts = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",
                                                              "placeholder":'Опишите свои мысли',
                                                            "rows":3}))
    emotions = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                             "placeholder":'Опишите свои эмоции',
                                                            "rows":3}))
    conclusion = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                             "placeholder": 'Опишите, к какому заключению вы пришли',
                                                              "rows":3}))

    class Meta:
        model = UserInfo
        fields = [ 'user','situation', 'thoughts', 'emotions', 'conclusion']


class DiaryRecordForm(forms.Form):
    #user_id = forms.IntegerField(label='user_id')
    situation = forms.CharField(label='situation', max_length=200)
    thoughts = forms.CharField(label='thoughts', max_length=300)
    emotions = forms.CharField(label='emotions', max_length=200)
    conclusion = forms.CharField(label='conclusion', max_length=200)
