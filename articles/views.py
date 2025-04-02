from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # new
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user # type: ignore

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article 
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user # type: ignore

class ArticleCreateView(LoginRequiredMixin, CreateView): #Mixin: to restrict editing without permission
    model = Article 
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author')

    def form_valid(self, form): #override the form_valid to specify one article to unique author
        form.instance.author = self.request.user
        return super().form_valid(form) #give the original from_valid the form we have 