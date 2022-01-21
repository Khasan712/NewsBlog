from django.db import models
from django.db.models.deletion import SET_NULL
from django_filters.utils import verbose_field_name
from hitcount.models import HitCountMixin
from config import settings

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from hitcount.models import HitCount

# Create your models here.
from mainapp.models import NewsPost


class CommentsPost(models.Model, HitCountMixin):
    post = models.ForeignKey(NewsPost, related_name='comments', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'comment_author',
        blank=True, null=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    def __str__(self):
        return '%s - %s' % (self.post.description, self.name)

    def children(self):
        return CommentsPost.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    class Meta:
        ordering = ['date']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"