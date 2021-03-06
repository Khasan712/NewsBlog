# Generated by Django 3.2.9 on 2021-12-11 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_remove_newspost_author'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('accounts', '0003_auto_20211210_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.categorypost')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
