from django import forms
from main.models import User_text
from django.utils.translation import gettext_lazy as _

class User_textForm(forms.ModelForm):
    """Form definition for User_text."""

    class Meta:
        """Meta definition for User_textform."""

        model = User_text
        fields = ('text', 'gif')
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type Here...',
                                           'class': 'userinput',}),
            'gif': forms.URLInput(attrs={'style': 'display:none;'}),
        }
        labels = {
            'text': _(''),
            'gif': _(''),
        }
