from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import Textarea
from .models import Contact
from .validators import validate_not_empty

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[validate_not_empty])
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=Textarea, validators=[validate_not_empty])
    is_answered = forms.BooleanField(initial=False)
    
    class Meta:
        # на основе какой модели создаётся класс формы
        model = Contact
        # укажем, какие поля будут в форме
        fields = ('name', 'email', 'subject', 'body')

        def clean_subject(self):
            data = self.cleaned_data['subject']

            if "спасибо" not in data.lower():
                raise forms.ValidationError("Вы обязательно должны нас поблагодарить!")
            return data