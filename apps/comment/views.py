from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Comment
from post.models import Post

def post_comment(request, postid, parent=None):
    post = get_object_or_404(Post, id=postid)

    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user

            if parent:
                parent_comment = Comment.objects.get(id=parent)
                new_comment.parent = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200')
            new_comment.save()
            return HttpResponse('200')
        else:
            return HttpResponse('400')