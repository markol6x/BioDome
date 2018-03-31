from django.conf.urls import url
from . import views

app_name = 'submission'

urlpatterns = [
    url(r'^atricles/$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^my_articles/$', views.MyArticleListView.as_view(), name='myarticle_list'),
    url(r'^(?P<slug>[-\w]+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^new/$', views.ArticleDataCreateView.as_view(), name='article_new'),
    url(r'^new/files/(?P<slug>[-\w]+)/$', views.ArticleFilesCreateView.as_view(), name='article_files_new'),
    url(r'^new/dataredirect/(?P<slug>[-\w]+)$', views.ArticleRedirectView.as_view(), name='redirect_data'),
    url(r'^new/confirm/(?P<slug>[-\w]+)/$', views.ArticleSubmitCreateView.as_view(), name='article_submit_new'),
    url(r'^thankyou/(?P<slug>[-\w]+)/$', views.ArticleSubmittedThankyouTemplateView.as_view(), name='article_submitted_thankyou'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.ArticleUpdateView.as_view(), name='article_edit'),
    url(r'^remove/(?P<slug>[-\w]+)/$', views.ArticleDeleteView.as_view(), name='article_remove'),
    url(r'^search/$', views.ArticleSearchListView.as_view(), name='article_search_list'),
    
    url(r'^confirm/(?P<slug>[-\w]+)$', views.submission_conf_view, name='article_confirm_detail'),
]
