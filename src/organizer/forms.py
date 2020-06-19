"""Forms for the Organizer app"""
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .models import Wod, Tag

class LowercaseNameMixin:
    """Form cleaner to lower case of name field"""

    def clean_name(self):
        """Ensure Tag name is always lowercase"""
        return self.cleaned_data["name"].lower()

class WodForm(ModelForm):
    """HTML form for Startup objects"""

    class Meta:
        model = Wod
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save wod'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-danger', ))

class TagForm(LowercaseNameMixin, ModelForm):
    """HTML form for Tag objects"""

    class Meta:
        model = Tag
        fields = "__all__"  # name only, no slug!
