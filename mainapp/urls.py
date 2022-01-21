from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('blog/entries', views.blog_entries, name="blog_entries"),
]