from django.urls import path
from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new, name="new"),
    path("search", views.search, name="search"),
    path("random", views.randomEntry, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
