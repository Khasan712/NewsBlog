from django.db.models import query
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

# Create your views here.
from .models import (
    CategoryPost,
    NewsPost
)
from .forms import ContactForm
from .filters import NewsPostFilter
# from comments.models import CommentsPost




def index(request):
    lastNews = NewsPost.objects.all().order_by('-date')
    lastFourNews = NewsPost.objects.all().order_by('-date')[:4]
    moreViews = NewsPost.objects.all().order_by('-hit_count_generic__hits')
    category = request.GET.get('category')
    
    if category == None:
        lastFourNews = NewsPost.objects.all().order_by('-date')[:4]
    else:
        moreViews = NewsPost.objects.filter(category__title=category).order_by('-hit_count_generic__hits')
    categories = CategoryPost.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        moreViews = moreViews.filter(Q(description__icontains=search) | Q(message__icontains=search) | Q(date__icontains=search))
    else:
        moreViews = NewsPost.objects.all().order_by('-hit_count_generic__hits')

    context = {
        'lastNews':lastNews,
        'moreViews':moreViews,
        'lastFourNews':lastFourNews,
        'categories':categories,
        # 'postNewsFilter':postNewsFilter,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def blog_entries(request):
    postNews = NewsPost.objects.all().order_by('-date')
    lastThreeNews = NewsPost.objects.all()[:3]
    category = request.GET.get('category')
    if category == None:
        postNews = NewsPost.objects.all().order_by('-date')
        postNewsFilter = NewsPostFilter(request.GET, queryset=NewsPost.objects.all().order_by('-hit_count_generic__hits'))
        postNews = postNewsFilter.qs
    else:
        postNews = NewsPost.objects.filter(category__title=category).order_by('-date')
    categories = CategoryPost.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        postNews = postNews.filter(Q(description__icontains=search) | Q(message__icontains=search) | Q(date__icontains=search))
    else:
        postNews = NewsPost.objects.all().order_by('-date')
    # Pagination part
    pagination = Paginator(postNews, 6)
    page = request.GET.get('page')
    postNews = pagination.get_page(page)


    context = {
        'postNews':postNews,
        'categories':categories,
        'postNewsFilter':postNewsFilter,
        'lastThreeNews':lastThreeNews
    }
    return render(request, 'blog.html', context)





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)
