import http.client

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.views import defaults

from . import models, forms


def index(request):
    slides_l = models.Post.objects.filter(promote=True).all().order_by('-views')[1:3]
    slide_r = models.Post.objects.filter(promote=True).all().order_by('-views').first()

    if request.method == 'POST':
        searched = request.POST['search']
        posts = models.Post.objects.all().order_by('-published_date').filter(
            Q(title__icontains=searched) | Q(text__icontains=searched))
    else:
        posts = models.Post.objects.all().order_by('-published_date')

    # myFilter = TitleSearch(request.GET, queryset=posts)
    # posts = myFilter.qs

    p = Paginator(posts, 8)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request, 'mysite/main.html', {'slides_l': slides_l, 'slide_r': slide_r, 'page_obj': page_obj})


def article(request):
    posts = models.Post.objects.all().order_by('-published_date')
    aside_lasts = models.Post.objects.all().order_by('-published_date')[:5]
    aside_populars = models.Post.objects.all().order_by('-views')[:5]

    result = request.GET.get('mosted')
    date_start = None
    date_end = None

    if result == 'view_mosted':
        posts = models.Post.objects.all().order_by('-views')

    elif result == 'view_least':
        posts = models.Post.objects.all().order_by('views')

    elif result == 'comment_order':
        posts = models.Post.objects.all().order_by('-commentCount')

    elif result == 'post_newest':
        posts = models.Post.objects.all().order_by('-published_date')

    elif result == 'post_oldest':
        posts = models.Post.objects.all().order_by('published_date')

    if request.GET.get('date_start'):
        date_start = request.GET.get('date_start')
        # return HttpResponse(date_start)
        posts = models.Post.objects.all().filter(Q(published_date__gte=date_start))

    if request.GET.get('date_end'):
        date_end = request.GET.get('date_end')
        # return HttpResponse(date_end)
        posts = models.Post.objects.all().filter(Q(published_date__lte=date_end))

    # myFilter = AsideFilter(request.GET, queryset=posts)
    # posts = myFilter.qs
    if request.method == 'POST':
        searched = request.POST['search']
        posts = models.Post.objects.all().order_by('-published_date').filter(
            Q(title__icontains=searched) | Q(text__icontains=searched))

    p = Paginator(posts, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return render(request, 'mysite/Articles.html',
                  {'date_start': date_start, 'date_end': date_end, 'page_obj': page_obj, 'aside_lasts': aside_lasts,
                   'aside_populars': aside_populars, 'result': result})


def detail(request, pk):
    aside_lasts = models.Post.objects.all().order_by('-published_date')[:5]
    aside_populars = models.Post.objects.all().order_by('-views')[:5]
    post_d = models.Post.objects.get(pk=pk)
    post_d.views += 1
    post_d.save()
    comments = models.Comment.objects.all().filter(Q(active=True) & Q(post=post_d))
    return render(request, 'mysite/detail.html',
                  {'post_d': post_d, 'aside_lasts': aside_lasts, 'aside_populars': aside_populars,
                   'comments': comments})


def sign(request):
    return render(request, 'mysite/sign-log.html')


def comment(request, pk):
    post = models.Post.objects.get(pk=pk)
    form = forms.CommentForm(request.POST)
    if form.is_valid():
        parent = None
        try:
            parentId = int(request.POST.get('parent_id'))
        except:
            parentId = None

        if parentId:
            parent = models.Comment.objects.get(id=parentId)
            if parent:
                sub_Comment = form.save(commit=False)
                sub_Comment.parent = parent

        instance = form.save(commit=False)
        instance.post = post
        post.commentCount += 1
        # post.save()
        instance.save()
    else:
        raise Exception('not valid')

    return redirect('detail', pk)


# def sub_comment(request, pk):
#     post = models.Post.objects.get(pk=pk)
#     form = forms.CommentForm(request.POST)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.post = post
#         post.commentCount += 1
#         # post.save()
#         instance.save()
#     else:
#         raise Exception('not valid')
#
#     return redirect('detail', pk)


# def search(request):


def handel404(request, exception):
    return render(request, 'mysite/404.html')


def handel403(request, exception):
    return render(request, 'mysite/403.html')


def handel400(request, exception):
    return render(request, 'mysite/400.html')


def handel500(request):
    return render(request, 'mysite/500.html')
