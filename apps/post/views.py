from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from post.models import Post, Tag, Category

import markdown


def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def archives(request, year, month):
    posts = Post.objects.filter(pub_time__year=year,
                                pub_time__month=month).order_by('-pub_time')
    return render(request, 'post/index.html', {'posts': posts})


def category(request, pk):
    cate = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=cate).order_by('-pub_time')
    return render(request, 'post/index.html', {'posts': posts})


def tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    posts = Post.objects.filter(tags=tag).order_by('-pub_time')
    return render(request, 'post/index.html', {'posts': posts})


class IndexView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_Object_name = 'posts'
    paginate_by = 5
    # def pagination_data(self, paginator, page, is_paginated):
    #     if not is_paginated:
    #         return {}
    #     left = []
    #     right = []
    #     left_has_more = []
    #     right_has_more = []
    #     first = False
    #     last = False
    #     page_num = page.number
    #     total = paginator.num_pages
    #
    #     page_range = paginator.page_range
    #
    #     if page_num == 1:
    #         right = page_range[page_num: page_num+2]
    #         if right[-1] < total -1:
    #             right_has_more = True
    #         if right[-1] < total:
    #             last = True
    #
    #     elif page_num == total:
    #         left = page_range[page_num - 3 if page_num - 3 > 0 else page_num-1]
    #         if left[0] > 2:
    #             left_has_more = True
    #         if left[0] > 1:
    #             first = True
    #     else:
    #         left = page_range[(page_num - 3) if (page_num - 3) > 0 else 0:page_num - 1]
    #         right = page_range[page_num:page_num + 2]
    #         if right[-1] < total- 1:
    #             right_has_more = True
    #         if right[-1] < total:
    #             last = True
    #         if left[0] > 2:
    #             left_has_more = True
    #         if left[0] > 1:
    #             first = True
    #
    #     data = {
    #         'left': left,
    #         'right': right,
    #         'left_has_more': left_has_more,
    #         'right_has_more': right_has_more,
    #         'first': first,
    #         'last': last,
    #     }
    #
    #     return data


class TagView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = super(PostDetailView, self).get_object(queryset=None)
        comments = post.comments.all()
        context.update({'comments': comments})
        return context


# class PostView():
#     def get(self):
#         return
#
#
# def index(request):
#     posts = Post.objects.all().order_by('-created_time')
#     return render(request, 'base.html', context={'posts': posts})
#
#
# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     comments = post.comments.all()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       'markdown.extensions.toc'
#                                   ])
#     return render(request, 'detail.html', {
#         'post': post,
#         'comments': comments
#     })

