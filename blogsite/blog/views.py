from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category


# Search view
def search_posts(request):
    """
    Search for blog posts by title or content using a query string.
    """
    query = request.GET.get("q", "")
    posts = []

    if query.strip():
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by("-created_at")

    return render(
        request,
        "blog/search_results.html",
        {
            "posts": posts,
            "query": query,
        },
    )


# View for listing all posts
def post_list(request):
    """
    Display all blog posts, newest first, along with all categories.
    """
    posts = Post.objects.all().order_by("-created_at")
    categories = Category.objects.all()

    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "categories": categories,
        },
    )


# View for displaying posts under a specific category
def category_posts(request, slug):
    """
    Display posts belonging to a specific category.
    """
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by("-created_at")

    return render(
        request,
        "blog/category_posts.html",
        {
            "category": category,
            "posts": posts,
        },
    )


# View for showing a single blog post
def post_detail(request, slug):
    """
    Show details of a single blog post.
    """
    post = get_object_or_404(Post, slug=slug)
    latest_posts = Post.objects.exclude(id=post.id).order_by("-created_at")[:5]

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "latest_posts": latest_posts,
        },
    )
