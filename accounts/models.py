from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


# Create your models here.


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='media', blank=True, null=True)
    back_img = models.ImageField(upload_to='media', blank=True, null=True)
    tel = PhoneField(blank=True)
    address = models.CharField(max_length=500, blank=True)
    website = models.URLField(max_length=200, blank=True)

    @property
    def get_img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
        else:
            return "/static/assets/user-profile-image/user.png"

    @property
    def get_back_img_url(self):
        if self.back_img and hasattr(self.back_img, 'url'):
            return self.back_img.url
        else:
            return ""