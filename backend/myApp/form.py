from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
