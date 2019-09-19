__author__ = 'Frank Shen'

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser
from django import forms


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'txt tabInput', 'placeholder': '密码，4-16位数字/字母/特殊符号（空格除外）'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'txt tabInput', 'placeholder': '重复密码'
        })

    class Meta(UserCreationForm):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('mobile',)
        widgets = {
            'mobile': forms.widgets.TextInput(attrs={
                'class': 'txt tabInput',
                'placeholder': '手机号'
            }),
            'username': forms.widgets.TextInput(attrs={
                'class': 'txt tabInput',
                'placeholder': '用户名'
            })
        }


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': '用户名'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': '密码，4-16位数字/字母/特殊符号（空格除外）'
        })