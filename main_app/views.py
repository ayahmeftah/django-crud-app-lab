from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Electronic
from .forms import OwnerForm, ElectronicForm
from django.shortcuts import render, redirect

def home(request):
    return render(request,'home.html')

# Owners Views
class OwnerListView(ListView):
    model = Owner
    template_name = "owners/owner_list.html"
    context_object_name = "owners"


class OwnerDetailView(DetailView):
    model = Owner
    template_name = "owners/owner_detail.html"
    context_object_name = "owner"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['electronics'] = Electronic.objects.filter(owner=self.object)
        return ctx


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "owners/owner_form.html"
    success_url = reverse_lazy("owner_list")


class OwnerUpdateView(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "owners/owner_form.html"

    def get_success_url(self):
        return reverse("owner_detail", kwargs={"pk": self.object.pk})


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = reverse_lazy("owner_list")



# Electronics Views
class ElectronicDetailView(DetailView):
    model = Electronic
    template_name = "electronics/electronic_detail.html"
    context_object_name = "electronic"
    pk_url_kwarg = "electronic_id"


class ElectronicCreateView(CreateView):
    model = Electronic
    form_class = ElectronicForm
    template_name = "electronics/electronic_form.html"

    def get_success_url(self):
        return reverse("owner_detail", kwargs={"pk": self.object.owner.pk})


class ElectronicUpdateView(UpdateView):
    model = Electronic
    form_class = ElectronicForm
    template_name = "electronics/electronic_form.html"
    pk_url_kwarg = "electronic_id"

    def get_success_url(self):
        return reverse("electronic_detail", kwargs={"electronic_id": self.object.pk})


class ElectronicDeleteView(DeleteView):
    model = Electronic
    pk_url_kwarg = "electronic_id"

    def get_success_url(self):
        return reverse("owner_detail", kwargs={"pk": self.object.owner.pk})

class ElectronicListView(ListView):
    model = Electronic
    template_name = "electronics/electronic_list.html"
    context_object_name = "electronics"
