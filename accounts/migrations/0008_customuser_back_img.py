# Generated by Django 3.2.9 on 2021-12-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_delete_usernewspost'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='back_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
