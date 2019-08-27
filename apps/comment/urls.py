__author__ = 'Frank Shen'

from django.urls import path
from .views import post_comment

app_name = 'comment'
urlpatterns = [
    path('post-comment/', post_comment, name='comment'),
]