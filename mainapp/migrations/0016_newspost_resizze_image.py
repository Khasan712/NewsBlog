# Generated by Django 3.2.9 on 2021-12-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_newspost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='resizze_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
