from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("group", "text")

    def clean_post(self):
        data = self.cleaned_data["text"]
        if data == '':
            raise forms.ValidationError('Пожалуйста, заполните поле')
        return data
        