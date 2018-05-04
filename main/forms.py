from django import forms
from django.utils.translation import gettext_lazy as _

FONTS = (
    ('1', 'Option 1'),
    ('2', 'Option 2'),
    ('3', 'Option 3'),
)

class Customize(forms.Form):
    """Customize definition."""

    # TODO: Define form fields here
    font = forms.ChoiceField(choices=FONTS)
    