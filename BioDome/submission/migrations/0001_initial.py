# Generated by Django 2.0.1 on 2018-03-14 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import submission.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('keywords', models.CharField(max_length=100)),
                ('article_type', models.CharField(choices=[('research', 'Research'), ('review', 'Review')], max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('authors', models.CharField(max_length=500)),
                ('abstract', models.TextField(max_length=500)),
                ('introduction', models.CharField(max_length=10000)),
                ('results', models.CharField(max_length=10000)),
                ('discussion', models.CharField(max_length=10000)),
                ('methods', models.CharField(max_length=10000)),
                ('references', models.CharField(max_length=10000)),
                ('fig_legends', models.CharField(max_length=10000)),
                ('main_file', models.FileField(upload_to=submission.validators.docx_path_handler, validators=[submission.validators.ExtensionValidator(['docx'])])),
                ('figure_1', models.ImageField(upload_to=submission.validators.fig1_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('figure_2', models.ImageField(blank=True, null=True, upload_to=submission.validators.fig2_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('figure_3', models.ImageField(blank=True, null=True, upload_to=submission.validators.fig3_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('figure_4', models.ImageField(blank=True, null=True, upload_to=submission.validators.fig4_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('figure_5', models.ImageField(blank=True, null=True, upload_to=submission.validators.fig5_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('figure_6', models.ImageField(blank=True, null=True, upload_to=submission.validators.fig6_path_handler, validators=[submission.validators.ExtensionValidator(['jpg', 'jpeg'])])),
                ('supplementary_file', models.FileField(blank=True, null=True, upload_to=submission.validators.suppl_path_handler, validators=[submission.validators.ExtensionValidator(['pdf'])])),
                ('submission_progress', models.IntegerField(default=0)),
                ('accept_conditions', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
