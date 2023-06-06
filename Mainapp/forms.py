from django import forms
from .models import WriteaBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = WriteaBlog
        fields = ('blog_title', 'blog_content', 'blog_image')