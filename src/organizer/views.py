"""Views for Organizer App"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import WodForm, TagForm
from .models import Wod, Tag

# Create your views here.
class WodCreate(CreateView):
    """Create new Wods via HTML form"""

    form_class = WodForm
    model = Wod
    template_name = "wod/form.html"
    extra_context = {"update": False}

class WodDelete(DeleteView):
    """Confirm and delete a Wod via HTML Form"""

    model = Wod
    template_name = "wod/confirm_delete.html"
    success_url = reverse_lazy("wod_list")

class WodList(ListView):
    """Display a list of Wods"""

    queryset = Wod.objects.all()
    paginate_by = 30
    template_name = "wod/list.html"

class WodDetail(DetailView):
    """Display a single Wod"""

    queryset = Wod.objects.all()
    template_name = "wod/detail.html"

class WodUpdate(UpdateView):
    """Update a Wod via HTML form"""

    form_class = WodForm
    model = Wod
    template_name = "wod/form.html"

class TagList(ListView):
    """Display a list of Tags"""

    queryset = Tag.objects.all()
    template_name = "tag/list.html"


class TagDetail(DetailView):
    """Display a single Tag"""

    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagCreate(CreateView):
    """Create new Tags via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}


class TagUpdate(UpdateView):
    """Update a Tag via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}


class TagDelete(DeleteView):
    """Confirm and delete a Tag via HTML Form"""

    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy("tag_list")
