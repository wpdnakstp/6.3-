from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields  =['title', 'body']


# form을 기반으로 바로받기

