# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Home - List all posts
    path("", views.post_list, name="post_list"),
    # Posts by category
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    # Single post detail
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    # Search posts
    path("search/", views.search_posts, name="search_posts"),
    # -----------------------------
    # Optional routes for future use:
    # -----------------------------
    # # Posts by author
    # path("author/<str:username>/", views.posts_by_author, name="posts_by_author"),
    # # Posts by tag
    # path("tag/<slug:slug>/", views.posts_by_tag, name="posts_by_tag"),
    # # Archive by year and month
    # path("archive/<int:year>/<int:month>/", views.archive_posts, name="archive_posts"),
    # # Static pages
    # path("about/", views.about_page, name="about"),
    # path("contact/", views.contact_page, name="contact"),
]
