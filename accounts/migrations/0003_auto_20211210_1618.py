# Generated by Django 3.2.9 on 2021-12-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]