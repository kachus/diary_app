from django import forms
from django.forms import ModelForm
from .models import UserInfo
from django.utils.translation import gettext_lazy as _

class TestForm(forms.Form):
    id = forms.CharField(label='id')
    username = forms.CharField(label='Username')


class UserInfoForm(ModelForm):
    labels = {
        'user': 'User',
        'situation': 'Что произошло?',
        'thoughts': 'О чем ты подумал/а?',
        'emotions': 'Какие эмоции испытал/а?',
        'conclusion': 'Какой вывод ты можешь сделать?'

    }
    emotions = forms.CharField(label=labels['emotions'], widget=forms.Textarea(attrs={"class": "form-control",
                                                            "placeholder": 'Опишите свои эмоции',
                                                            "rows": 4,
                                                                            }))

    situation = forms.CharField(label=labels['situation'], required=True, widget=forms.Textarea(attrs={"class":"form-control",
                                                              "placeholder":'Опишите ситуацию',
                                                              "rows":3,
                                                              }))
    thoughts = forms.CharField(label = labels['thoughts'],widget=forms.Textarea(attrs={"class":"form-control",
                                                              "placeholder":'Опишите свои мысли',
                                                            "rows":4}))

    conclusion = forms.CharField(label=labels['conclusion'],widget=forms.Textarea(attrs={"class": "form-control",
                                                             "placeholder": 'Опишите, к какому заключению вы пришли',
                                                              "rows":3,
                                                              }))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


    class Meta:
        model = UserInfo
        fields = ('situation', 'thoughts', 'emotions', 'conclusion')
        # widgets = {
        #
        #     'situation' : forms.Textarea(attrs={"class":"form-control",
        #                                                  "placeholder":'Опишите ситуацию',
        #                                                  "rows":3,
        #                                                   }),
        # }
        labels = {
            'user': 'User',
            'situation' : 'Что произошло?',
            'thoughts' : 'О чем ты подумал/а?',
            'emotions' : 'Какие эмоции испытал/а?',
            'conclusion' : 'Какой вывод ты можешь сделать?'

        }




class DiaryRecordForm(forms.Form):
    #user_id = forms.IntegerField(label='user_id')
    situation = forms.CharField(label='situation', max_length=200)
    thoughts = forms.CharField(label='thoughts', max_length=300)
    emotions = forms.CharField(label='emotions', max_length=200)
    conclusion = forms.CharField(label='conclusion', max_length=200)
