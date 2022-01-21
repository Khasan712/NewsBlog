from django.contrib import admin

# Register your models here.
from .models import (
    CategoryPost,
    NewsPost,
    Contact
)

class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(CategoryPost, CategoryPostAdmin)


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'category', 'description', 'date']
admin.site.register(NewsPost, NewsPostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
admin.site.register(Contact, ContactAdmin)
