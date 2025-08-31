from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Owner, Electronic
from .forms import OwnerForm, ElectronicForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Home page
def home(request):
    return render(request, 'home.html')


# Owners Views
class OwnerListView(LoginRequiredMixin, ListView):
    model = Owner
    template_name = "owners/owner_list.html"
    context_object_name = "owners"

    def get_queryset(self):
        return Owner.objects.filter(user=self.request.user)

class OwnerDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Owner
    template_name = "owners/owner_detail.html"
    context_object_name = "owner"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['electronics'] = Electronic.objects.filter(owner=self.object)
        return ctx

    def test_func(self):
        owner = self.get_object()
        return owner.user == self.request.user

class OwnerCreateView(LoginRequiredMixin, CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "owners/owner_form.html"
    success_url = reverse_lazy("owner_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "owners/owner_form.html"

    def get_success_url(self):
        return reverse("owner_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        owner = self.get_object()
        return owner.user == self.request.user

class OwnerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Owner
    success_url = reverse_lazy("owner_list")

    def test_func(self):
        owner = self.get_object()
        return owner.user == self.request.user



# Electronics Views
class ElectronicListView(LoginRequiredMixin, ListView):
    model = Electronic
    template_name = "electronics/electronic_list.html"
    context_object_name = "electronics"

    def get_queryset(self):
        return Electronic.objects.filter(owner__user=self.request.user)


class ElectronicDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Electronic
    template_name = "electronics/electronic_detail.html"
    context_object_name = "electronic"
    pk_url_kwarg = "electronic_id"

    def test_func(self):
        electronic = self.get_object()
        return electronic.owner.user == self.request.user


class ElectronicCreateView(LoginRequiredMixin, CreateView):
    model = Electronic
    form_class = ElectronicForm
    template_name = "electronics/electronic_form.html"
    success_url = reverse_lazy("electronic_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['owner'].queryset = Owner.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        owner = form.cleaned_data.get('owner')
        if owner.user != self.request.user:
            return self.handle_no_permission()
        form.instance.owner = owner
        return super().form_valid(form)


class ElectronicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Electronic
    form_class = ElectronicForm
    template_name = "electronics/electronic_form.html"
    pk_url_kwarg = "electronic_id"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['owner'].queryset = Owner.objects.filter(user=self.request.user)
        return form

    def get_success_url(self):
        return reverse("electronic_detail", kwargs={"electronic_id": self.object.pk})

    def test_func(self):
        electronic = self.get_object()
        return electronic.owner.user == self.request.user


class ElectronicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Electronic
    pk_url_kwarg = "electronic_id"
    success_url = reverse_lazy("electronic_list")

    def test_func(self):
        electronic = self.get_object()
        return electronic.owner.user == self.request.user

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/sign-up.html'
