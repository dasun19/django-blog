from django.contrib import admin
from .models import Post
# Register your models here.
from .models import Category, Post, Comment, Reply

admin.site.register(Category)
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)

@admin.register(Post)  # Use the decorator to register the Post model
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author', 'category')  # Customize the admin display
    search_fields = ('title', 'content')  # Add search functionality
    list_filter = ('date_posted', 'category')  # Add filters