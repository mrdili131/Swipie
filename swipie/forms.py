from django import forms
from .models import Post

class SearchForm(forms.Form):
    query = forms.CharField()


class PostUpload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','text']