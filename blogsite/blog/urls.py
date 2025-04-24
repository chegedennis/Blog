# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
