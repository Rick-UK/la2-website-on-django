from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from la2.models import News


# Create your views here.
def index(request):
    list_of_news = News.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(list_of_news, 5)
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    request.session['get_back_url_news'] = request.get_full_path()

    return render(request, 'la2/index.html', {'list_of_news':news_list})

def news_detail_page(request,news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'la2/news_detail_page.html', {'news':news})

def play_page(request):
    return render(request, 'la2/play_page.html')

def donate_page(request):
    return render(request, 'la2/donate_page.html')