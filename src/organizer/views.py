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

from .forms import WodForm
from .models import Wod

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
