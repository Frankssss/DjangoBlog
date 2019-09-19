from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

from .forms import MyUserCreationForm, MyAuthenticationForm
from .models import MyUser
from .send_mail import send_ack_mail, make_confirm_string


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
                data['status'] = 'SUCCESS'
        else:
            data['status'] = 'ERROR'
            data['msg'] = list(form.errors.values())[0]
        return JsonResponse(data)
    return render(request, 'user/login.html', locals())


def registerView(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        data = {}
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            # if MyUser.objects.filter(Q(email=username) | Q(username=username)):
            #     user = MyUser.objects.filter(Q(email=username) | Q(username=username)).first()
            #     login(request, user)
            data['status'] = 'SUCCESS'
            data['msg'] = '注册成功, 请确认邮件'
            
            code = make_confirm_string(user)
            send_ack_mail(email, code)
        else:
            data['status'] = 'ERROR'
            data['msg'] = list(form.errors.values())[0][0]
        return JsonResponse(data)
    return render(request, 'user/register.html', locals())


def logoutView(request):
    logout(request)
    return redirect('post:index')

