from django.contrib import admin
from blog.models import About, Category, Post

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(About)