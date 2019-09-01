from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.urls import reverse

from .forms import CommentForm
from .models import Comment

from post.models import Post


def post_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('post:index'))
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, user=request.user)
        if comment_form.is_valid():
            new_comment = Comment()
            new_comment.post = comment_form.cleaned_data['post']
            new_comment.user = comment_form.cleaned_data['user']
            parent = comment_form.cleaned_data['parent']
            try:
                parent = int(parent)
                if parent > 0:
                    comment = Comment.objects.get(id=parent)
                    new_comment.parent = comment
            except Exception as e:
                pass
            new_comment.content = comment_form.cleaned_data['content']
            new_comment.save()
            return redirect(referer)
        else:
            return HttpResponse("400")