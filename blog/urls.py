from django.urls import path
from . import views
from blog.views import BlogView,BlogDetailView,Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('blog/',BlogView.as_view(), name = "blog"),
    path('blog-detail/<int:pk>',BlogDetailView.as_view(), name='blog-detail'),

]
