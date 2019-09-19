from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

from .forms import MyUserCreationForm, MyAuthenticationForm
from .models import MyUser


def loginView(request):
    form = MyAuthenticationForm()
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        data = {}
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            if MyUser.objects.filter(Q(mobile=username)| Q(username=username)):
                user = MyUser.objects.filter(Q(mobile=username) | Q(username=username)).first()
                login(request, user)
                ata['status'] = 'SUCCESS'
        else:
            data['status'] = 'ERROR'
            data['msg'] = list(form.errors.values())[0]
        return JsonResponse(data)
    return render(request, 'user/login.html', locals())


def registerView(request):
    user = MyUserCreationForm(request.POST)
    if request.method == 'POST':
        if user.is_valid():
            user.save()
            tips = '注册成功'
        else:
            if user.errors.get('username', ''):
                tips = user.errors.get('username', '注册失败')
            else:
                tips = user.errors.get('mobile', '注册失败')
    return render(request, 'user/register.html', locals())


def logoutView(request):
    logout(request)
    return redirect('post:index')

