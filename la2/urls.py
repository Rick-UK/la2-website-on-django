from django.urls import path
from . import views

app_name = 'la2'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/<slug:news_slug>/', views.news_detail_page, name='news_detail_page'),
    path('play/', views.play_page, name='play_page'),
    path('donate/', views.donate_page, name='donate_page'),
    path('about/', views.about_page, name='about_page'),
    path('feedback/', views.feedback_page, name='feedback_page'),
]