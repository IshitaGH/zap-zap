from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Target

# Create your views here.
def home(request):
    context = {
        'targets': Target.objects.all()
    }
    return render(request, 'photo_upload/home.html', context)

# class PostListView(ListView):
#     model = Target
#     template_name = 'photo_upload/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5


class UserPostListView(ListView):
    model = Target
    template_name = 'photo_upload/user_target.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'target'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Target.objects.filter(author=user).order_by('-target_name')


class PostDetailView(DetailView):
    model = Target


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Target
    fields = ['target_name', 'image', 'call_police', 'ring_alarm', 'message_contacts', 'message_to_contacts']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Target
    fields = ['target_name', 'image', 'call_police', 'ring_alarm', 'message_contacts', 'message_to_contacts']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Target
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False