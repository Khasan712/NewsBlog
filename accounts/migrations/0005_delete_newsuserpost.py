# Generated by Django 3.2.9 on 2021-12-11 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_newsuserpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsUserPost',
        ),
    ]
