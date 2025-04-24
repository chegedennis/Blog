from django.contrib import admin
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    content = CKEditorWidget()  # Use CKEditorWidget for content field

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
