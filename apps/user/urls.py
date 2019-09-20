__author__ = 'Frank Shen'

from django.urls import path

from .views import loginView, logoutView, registerView, user_confirm

app_name = 'user'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('register', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('confirm/', user_confirm, name='confirm')
]