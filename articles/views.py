from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "body", "author"]
    template_name = "article_create.html"



class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleEditView(UpdateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article_edit.html"
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = "/articles/"
    template_name = "article_delete.html"
    context_object_name = "article"
