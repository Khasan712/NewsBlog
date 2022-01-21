from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import CommentsPost

class CommentsPostForm(forms.ModelForm):
    class Meta:
        model = CommentsPost
        fields = ('message',)