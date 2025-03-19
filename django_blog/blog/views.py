from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Category,Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import SearchForm, CommentForm, ReplyForm, PostForm

# Create your views here.




# def home(request):
#
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, "blog/home.html", context)
#
def about(request):
     return render(request, "blog/about.html", {'title':'Blog About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(tags__name__icontains=query).distinct()
        category = self.request.GET.get('category')  # Retrieve the category ID from the request
        if category:  # Check if a category filter is applied
            queryset = queryset.filter(category__id=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')

        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-date_posted')  # Get comments for the post
        context['comment_form'] = CommentForm()  # Add the comment form to the context
        context['reply_form'] = ReplyForm()  # Add the reply form to the context
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:  # Handle comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = self.object
                comment.author = request.user
                comment.save()
                messages.success(request, 'Your comment has been added.')
                return redirect('blog-detail', pk=self.object.pk)
        elif 'reply_submit' in request.POST:  # Handle reply submission
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
                reply.author = request.user
                reply.save()
                messages.success(request, 'Your reply has been added.')
                return redirect('blog-detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content', 'image', 'category', 'tags']
#     template_name = 'blog/post_form.html'
#     login_url = reverse_lazy('login')  # Redirects to the login URL if not authenticated

#     def get_form(self):
#         form = super().get_form()
#         form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'})
#         form.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your content here...'})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'category', 'tags']  # Ensure 'image' is included
    template_name = 'blog/post_form.html'
    login_url = reverse_lazy('login')  # Redirects to the login URL if not authenticated

    def get_form(self):
        form = super().get_form()
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'})
        form.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your content here...'})
        form.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control'})  # Add styling for the image field
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'category', 'tags']  # Ensure 'image' is included
    login_url = reverse_lazy('login')

    def get_form(self):
        form = super().get_form()
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update title here'})
        form.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Update your content here...'})
        form.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control'})  # Add styling for the image field
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to update this post.')
        return redirect('home')
        return form

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.object.pk})

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content', 'image', 'category', 'tags']
#     login_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('blog-detail', kwargs={'pk': self.object.pk})

#     def test_func(self):
#         post = self.get_object()

#         if self.request.user == post.author:
#             return True

#         return False

#     def handle_no_permission(self):
#         messages.error(self.request, 'You are not authorized to update this post.')
#         return redirect('home')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True

        return False

    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to delete this post.')
        return redirect('home')
