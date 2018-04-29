from django import forms


class User_textForm(forms.ModelForm):
    """Form definition for User_text."""

    class Meta:
        """Meta definition for User_textform."""

        model = User_text
        fields = ('text', 'gif')
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Write Something',
                                           'class': 'userinput'}),
            'gif': forms.URLInput(attrs={'style': 'display:none;'}),
        }
