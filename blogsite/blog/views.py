from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# View for all posts
def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


# View for posts by category
def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(
        request, "blog/category_posts.html", {"category": category, "posts": posts}
    )


# View for single post
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
