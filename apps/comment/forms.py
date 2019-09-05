__author__ = 'Frank Shen'

from django import forms
from post.models import Post
from ckeditor.fields import CKEditorWidget
from django.db.models import ObjectDoesNotExist

from .models import Comment


class CommentForm(forms.Form):
    parent = forms.CharField(widget=forms.HiddenInput)
    post_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(widget=CKEditorWidget(config_name='comment_config'),
                              error_messages={'required': '评论内容不能为空.'}
                              )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')
        post_id = self.cleaned_data['post_id']
        try:
            post = Post.objects.get(id=post_id)
            self.cleaned_data['post'] = post
        except ObjectDoesNotExist as e:
            raise forms.ValidationError('文章不存在')
        return self.cleaned_data

    def clean_parent(self):
        parent = int(self.cleaned_data['parent'])
        if parent < 0:
            raise forms.ValidationError('回复出错')
        elif parent == 0:
            self.cleaned_data['parent'] = None
        elif Comment.objects.filter(pk=parent).exists():
            self.cleaned_data['parent'] = Comment.objects.get(pk=parent)
        else:
            raise forms.ValidationError('回复出错')
        return self.cleaned_data['parent']
