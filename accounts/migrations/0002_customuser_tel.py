# Generated by Django 3.2.9 on 2021-12-10 11:15

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tel',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]