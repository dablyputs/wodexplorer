from django.urls import reverse
from django.db.models import (
    AutoField,
    DateField,
    CharField,
    Model,
    TextField,
    URLField,
)


class Wod(Model):
    coach = CharField(max_length=30, null=True)
    date = DateField(null=True)
    id = AutoField(
        primary_key=True
    )
    url = URLField(
        null=True,
        max_length=255  # https://tools.ietf.org/html/rfc3986,
    )
    workout = TextField(null=True)

    class Meta:
        get_latest_by = "date"
        ordering = ["date"]

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        """Return URL to detail page of Startup"""
        return reverse(
            "wod_detail", kwargs={"pk": self.pk}
        )
