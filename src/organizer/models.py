"""
Django data models for organizing scraped gym workout data

Django Model Documentation:
https://docs.djangoproject.com/en/2.2/topics/db/models/
https://docs.djangoproject.com/en/2.2/ref/models/options/
https://docs.djangoproject.com/en/2.2/internals/contributing/writing-code/coding-style/#model-style
Django Field Reference:
https://docs.djangoproject.com/en/2.2/ref/models/fields/
https://docs.djangoproject.com/en/2.2/ref/models/fields/#autofield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#charfield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#datefield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#emailfield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey
https://docs.djangoproject.com/en/2.2/ref/models/fields/#manytomanyfield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#slugfield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#textfield
https://docs.djangoproject.com/en/2.2/ref/models/fields/#urlfield

AutoSlugField Reference:
https://django-extensions.readthedocs.io/en/latest/field_extensions.html

"""

from django.urls import reverse
from django.db.models import (
    DateField,
    CASCADE,
    CharField,
    ForeignKey,
    Model,
    ManyToManyField,
    TextField,
    URLField,
)
from django_extensions.db.fields import AutoSlugField

class Coach(Model):
    name = CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.name)

class Gym(Model):
    name = CharField(max_length=30, null=True)
    website = URLField(
        max_length=255
    )

    def __str__(self):
        return str(self.name)

class Tag(Model):
    """Labels to help categorize data"""

    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["name"],
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Tag"""
        return reverse(
            "tag_detail", kwargs={"slug": self.slug}
        )

class Wod(Model):
    coach_link = ForeignKey(Coach, on_delete=CASCADE, editable=False)
    sched_date = DateField(
        editable=False,
        null=True
    )
    gym_link = ForeignKey(Gym, on_delete=CASCADE, editable=False)
    """The URL that the data was scraped from"""
    orig_url = URLField(
        editable=False,
        null=True,
        max_length=255  # https://tools.ietf.org/html/rfc3986,
    )
    workout = TextField(
        null=True,
        editable=False
    )
    tags = ManyToManyField(Tag, blank=True)

    class Meta:
        get_latest_by = "-sched_date"
        ordering = ["sched_date"]

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "wod_detail", kwargs={"pk": self.pk}
        )

