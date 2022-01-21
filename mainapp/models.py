from django.db import models
from taggit.managers import TaggableManager
from django.contrib.contenttypes.fields import GenericRelation
from config import settings
from hitcount.models import HitCount
from PIL import Image
from sorl.thumbnail import ImageField, get_thumbnail

class CategoryPost(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class NewsPost(models.Model):
    image = models.ImageField(upload_to='media')
    resizze_image = models.ImageField(upload_to='media', blank=True, null=True)
    # large_image = models.ImageField(upload_to='media', blank=True, null=True)
    category = models.ForeignKey(CategoryPost, on_delete=models.SET_NULL, blank=True, null=True)
    tags = TaggableManager(blank=True)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'author',
        blank=True, null=True
    )
    date = models.DateField(auto_now_add=True)
    message = models.TextField(blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    
    def save(self):
        super().save()
        if self.image:
            image_new = Image.open(self.image.path)
            if image_new.height >500 or image_new.width>500:
                new_size = (1500,500)
                image_new.thumbnail(new_size)
                print(image_new.height, image_new.width)
                image_new.save(self.image.path)


    def __str__(self):
        return self.description

    def get_count(self):
        return self.comments.count()
       


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email






