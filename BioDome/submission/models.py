from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
import uuid

from .validators import *

class Article(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    is_submitted = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    keywords = models.CharField(max_length=100)
    article_type = models.CharField(max_length=10, choices= (('research', 'Research'),('review', 'Review')))

    title = models.CharField(max_length=150)
    authors = models.CharField(max_length=500)
    abstract = models.TextField(max_length=500)
    introduction = models.CharField(max_length=10000)
    results = models.CharField(max_length=10000)
    discussion = models.CharField(max_length=10000)
    methods = models.CharField(max_length=10000)
    references = models.CharField(max_length=10000)
    fig_legends = models.CharField(max_length=10000)

    main_file = models.FileField(upload_to=docx_path_handler, validators=[ExtensionValidator(['docx'])])
    figure_1 = models.ImageField(upload_to=fig1_path_handler, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    figure_2 = models.ImageField(upload_to=fig2_path_handler, null=True, blank=True, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    figure_3 = models.ImageField(upload_to=fig3_path_handler, null=True, blank=True, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    figure_4 = models.ImageField(upload_to=fig4_path_handler, null=True, blank=True, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    figure_5 = models.ImageField(upload_to=fig5_path_handler, null=True, blank=True, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    figure_6 = models.ImageField(upload_to=fig6_path_handler, null=True, blank=True, validators=[ExtensionValidator(['jpg', 'jpeg'])])
    supplementary_file = models.FileField(upload_to=suppl_path_handler, null=True, blank=True, validators=[ExtensionValidator(['pdf'])])
    submission_progress = models.IntegerField(default=0)
    accept_conditions = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ''' this is a really weird solution but I don't want to fix it right now... '''
        article_instance = Article.objects.get(slug=self.slug)
        article_instance.submission_progress += 1
        article_instance.save()
        print (self.submission_progress)
        if int(self.submission_progress) == 0:
            return reverse('submission:article_files_new', kwargs={'slug': self.slug})
        elif self.submission_progress == 1:
            return reverse('submission:redirect_data', kwargs={'slug': self.slug})
        else:
            return reverse('submission:article_submitted_thankyou', kwargs={'slug': self.slug})

    @classmethod
    def submit_paper(self, slug):
        article_instance = Article.objects.get(slug=slug)
        print("submit_paper")
        handle = open("media/files/{id}/manuscript_{file}.html".format(id=slug, file=slug), 'r')
        manuscript_data = handle.read()
        handle.close()

        import regex

        article_instance.introduction = regex.findall('INTRODUCTION.+\n([.\s\S\n]*?)\n.+RESULTS', manuscript_data)[0]
        article_instance.results = regex.findall('RESULTS.+\n([.\s\S\n]*?)\n.*\n.*DISCUSSION', manuscript_data)[0]
        article_instance.discussion = regex.findall('DISCUSSION.+\n([.\s\S\n]*?)\n.*\n.*METHODS', manuscript_data)[0]
        article_instance.methods = regex.findall('METHODS.+\n([.\s\S\n]*?)\n.*\n.*REFERENCES', manuscript_data)[0]
        article_instance.references = regex.findall('REFERENCES.+\n([.\s\S\n]*?)\n.*\n.*FIGURE LEGENDS', manuscript_data)[0]
        article_instance.fig_legends = regex.findall('FIGURE LEGENDS.+\n([.\s\S\n]*?)$', manuscript_data)[0]


        article_instance.is_submitted = True
        article_instance.is_published = True
        article_instance.save()
        print()
        print(article_instance.submission_progress)

    @classmethod
    def convert_word(self, slug):
        article_instance = Article.objects.get(slug=slug)
        print("convert_word")
        article_instance.save()
        # print(article_instance.submission_progress)

        import pypandoc
        pypandoc.convert_file("media/files/{id}/manuscript_{file}.docx".format(id=slug, file=slug),
                              'html', outputfile="media/files/{id}/manuscript_{file}.html".format(id=slug, file=slug))
