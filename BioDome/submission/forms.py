from django import forms
from . models import Article

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ('title', 'authors', 'keywords',
                  'article_type', 'abstract', )

        labels = {
            'title': 'Article Title: Maximum allowed charachters is 150 (with spaces).',
            'authors': 'Authors: List all authors separated with , (Firstname Middlename Lastname, Firstname Lastname, Firstname MN Lastname, ... )',
            'article_type': 'Article Type:',
            'abstract': 'Abstract.  Maximum allowed charachters is 500 (with spaces).'
        }

        widgets = {'abstract': forms.Textarea(attrs={'rows':6,}),
        }

class ArticleFilesForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ('main_file', 'figure_1','figure_2', 'figure_3', 'figure_4', 'figure_5', 'figure_6', 'supplementary_file')

class ArticleSubmitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleSubmitForm, self).__init__(*args, **kwargs)
        self.fields['accept_conditions'].required = True
    class Meta():
        model = Article
        fields = ('accept_conditions', )
        labels = {
            'accept_conditions': 'Please read and accept terms of submission.',
        }
