from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    search,
    about
)

urlpatterns = [
    # Blog home page
    path('darslik/', PostListView.as_view(), name='blog-home'),
    
    # User's posts list
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    
    # Post detail view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Post creation view
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # Post update view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # Post delete view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Search view
    path('search/', search, name='search'),
    
    # About page
    path('about/', about, name='blog-about'),
]

from django.shortcuts import render

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)
