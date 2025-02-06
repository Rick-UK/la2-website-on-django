from django.urls import path
from . import views

app_name = 'la2'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/<slug:news_slug>/', views.news_detail_page, name='news_detail_page'),
]