from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

from .forms import MyUserCreationForm
from .models import MyUser


def loginView(request):
    user = MyUserCreationForm()
    if request.method == 'POST':
        loginUser = request.POST.get('loginUser', '')
        password = request.POST.get('password', '')
        if MyUser.objects.filter(Q(mobile=loginUser)| Q(username=loginUser)):
            user = MyUser.objects.filter(Q(mobile=loginUser) | Q(username=loginUser)).first()
            if check_password(password, user.password):
                login(request, user)
                return redirect('/')
            else:
                tips = '密码错误'
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

