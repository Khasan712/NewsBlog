from django.contrib import admin

# Register your models here.
from .models import CommentsPost



class CommentsPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'name', 'email', 'subject']
    list_filter = ['name', 'date']
    search_fields = ['name', 'email', 'message']
admin.site.register(CommentsPost, CommentsPostAdmin)
# admin.site.register(CommentsPost)








