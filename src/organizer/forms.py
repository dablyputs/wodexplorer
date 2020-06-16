"""Forms for the Organizer app"""
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import Wod

class WodForm(ModelForm):
    """HTML form for Startup objects"""

    class Meta:
        model = Wod
        fields = ['workout', 'coach', 'url', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save wod'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger', ))

