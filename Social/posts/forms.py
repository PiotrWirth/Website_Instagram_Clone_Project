from .models import Posts
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','image','caption')
        