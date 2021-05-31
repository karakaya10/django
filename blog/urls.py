from blog.models import Category
from blog.views import AboutView, BlogPageView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post'),
    path('about/',AboutView.as_view(template_name="about.html")),
    path('', BlogPageView.as_view(), name = 'index'),
]
