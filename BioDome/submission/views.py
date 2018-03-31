from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# import operator
from django.db.models import Q
from functools import reduce

# Create your views here.
class ArticleListView(ListView):
    model = Article
    def get_queryset(self):
        return Article.objects.filter().order_by('-created_date')

class MyArticleListView(ListView, LoginRequiredMixin):
    model = Article
    def get_queryset(self):
        return Article.objects.filter(author__exact=self.request.user).order_by('-created_date')

class ArticleSearchListView(ListView):
    model = Article
    def get_queryset(self):
        fields = ['title', 'abstract', 'authors']
        result = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(
                reduce(lambda x, y: x | Q(**{"{}__icontains".format(y): query}), fields, Q())
            )
        return result

class ArticleDetailView(DetailView):
    template_name = 'submission/article_detail.html'
    model = Article


class ArticleDataCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    model = Article
    template_name = "submission/article_form.html"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return HttpResponseRedirect(article.get_absolute_url())


class ArticleRedirectView(LoginRequiredMixin, RedirectView):
    # permanent = True
    pattern_name = 'submission:article_submit_new'  # the pattern to redirect to

    def get_redirect_url(self, *args, **kwargs):
        Article.convert_word(self.kwargs['slug'])
        Article.submit_paper(self.kwargs['slug'])


        return super().get_redirect_url(*args, **kwargs)
        # return super().get_absolute_url(*args, **kwargs)


class ArticleFilesCreateView(LoginRequiredMixin, UpdateView):
    form_class = ArticleFilesForm
    model = Article
    template_name = "submission/article_form.html"

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return HttpResponseRedirect(article.get_absolute_url())

class ArticleSubmitCreateView(LoginRequiredMixin, UpdateView):
    form_class = ArticleSubmitForm
    model = Article
    template_name = "submission/article_submit_form.html"
    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return HttpResponseRedirect(article.get_absolute_url())

class ArticleSubmittedThankyouTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'submission/article_submitted_thankyou.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'submission/article_confirm_detail.html'
    form_class = ArticleForm
    model = Article

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('submission:article_list')


def submission_conf_view(request, slug):
    Article.submit_paper(slug)
    Article.convert_word(slug)
    return redirect('submission:article_list')
