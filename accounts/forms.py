from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import CustomUser  
from mainapp.models import NewsPost, CategoryPost


class UserProfileForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class UserEditProfileForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'img', 'back_img', 'bio', 'tel', 'address', 'website']

class CategoryUserPost(forms.ModelForm):
    class Meta:
        model = CategoryPost
        fields = '__all__'


class CreatUserPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['image', 'category', 'tags', 'description', 'message']
        # widgets = {
        #     # 'image': forms.TextInput(attrs={'type':'file', 'id':'formFile'}),
        #     # 'category': forms.Select(attrs={'class':"dropdown",}),
        #     'tags': forms.TextInput(attrs={'class':'form-control'}),
        #     'description': forms.TextInput(attrs={'class':'form-control'}),
        #     'message': forms.Textarea(attrs={'cols': 47, 'rows': 10, 'class':'form-control'}),
        #     # 'author': forms.Select(attrs={'class':"form-control"}),
        # }