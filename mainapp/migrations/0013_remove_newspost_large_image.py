# Generated by Django 3.2.9 on 2021-12-11 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_newspost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='large_image',
        ),
    ]
