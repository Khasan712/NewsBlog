from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:pk>/details', views.post_details, name="post_details"),
]