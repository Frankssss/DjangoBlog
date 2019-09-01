from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from comment.forms import CommentForm

import markdown


class IndexView(ListView):
    model = Post
    template_name = 'article/index.html'
    context_object_name = 'post_list'
    paginate_by = 5


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


class ArchivesView(IndexView):
    def get_queryset(self):
        return super(ArchivesView, self).get_queryset().filter(pub_time__year=self.kwargs.get('year'),
                                                               pub_time__month=self.kwargs.get('month'))


class PostDetailView(DetailView):
    model = Post
    template_name = 'article/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = super(PostDetailView, self).get_object(queryset=None)
        comments = post.comments.all()
        comment_form = CommentForm(initial={'post_id': post.id, 'parent':0})
        context.update({'comments': comments, 'comment_form': comment_form})
        return context


def bad_request(request):
    return render(request, '400.html')


# def permission_denied(request):
#     return render(request, '403.html')

def test(request):
    from django.http import Http404, HttpResponse
    raise Http404("thissssss")


def page_not_found(request):
    return render(request, '404.html')


def error(request):
    return render(request, '500.html')

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
