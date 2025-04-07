from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.db.models import Q

from django.shortcuts import render

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

# Home page view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# Search functionality
def search(request):
    query = request.GET.get('q', '')  # Get query from GET parameters
    result = Post.objects.filter(
        Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)
    )
    context = {
        'posts': result,
        'query': query
    }
    return render(request, 'blog/home.html', context)


# File download view
def getfile(request, file_name):
    # Adjust this based on how your files are stored or served
    from django.contrib.staticfiles.views import serve
    return serve(request, file_name)


# Class-based views for Post list, detail, create, update, and delete

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Template to display all posts
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order by date_posted descending
    paginate_by = 10  # Pagination with 10 posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # Template to display user's posts
    context_object_name = 'posts'
    paginate_by = 10  # Pagination with 10 posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template to display post details


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template to create a new post
    fields = ['title', 'content', 'file']  # Fields to be included in the form

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template to edit a post
    fields = ['title', 'content', 'file']  # Fields to be included in the form

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the user is the author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to the homepage after successful deletion
    template_name = 'blog/post_confirm_delete.html'  # Template for confirming deletion

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# About page view
def about(request):
    return render(request, 'blog/about.html', {'title': 'Biz haqimizda'})
