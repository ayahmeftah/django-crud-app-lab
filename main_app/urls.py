from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    # Owners
    path("owners/", views.OwnerListView.as_view(), name="owner_list"),
    path("owners/<int:pk>/", views.OwnerDetailView.as_view(), name="owner_detail"),
    path("owners/add/", views.OwnerCreateView.as_view(), name="owner_create"),
    path("owners/<int:pk>/edit/", views.OwnerUpdateView.as_view(), name="owner_update"),
    path("owners/<int:pk>/delete/", views.OwnerDeleteView.as_view(), name="owner_delete"),

    # Electronics
    path("electronics/", views.ElectronicListView.as_view(), name="electronic_list"),
    path("electronics/<int:electronic_id>/", views.ElectronicDetailView.as_view(), name="electronic_detail"),
    path("electronics/add/", views.ElectronicCreateView.as_view(), name="electronic_create"),
    path("electronics/<int:electronic_id>/edit/", views.ElectronicUpdateView.as_view(), name="electronic_update"),
    path("electronics/<int:electronic_id>/delete/", views.ElectronicDeleteView.as_view(), name="electronic_delete"),
]
