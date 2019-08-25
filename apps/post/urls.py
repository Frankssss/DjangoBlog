__author__ = "Frank Shen"

from django.urls import path
from post.views import IndexView, PostDetailView, index, archives, category, tag

app_name = 'post'
urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/<int:year>/<int:month>/', archives, name='archives'),
    path('category/<int:pk>/', category, name='category'),
    path('tag/<int:pk>/', tag, name='tag')
]