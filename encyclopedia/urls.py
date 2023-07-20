from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new, name="new"),
    # query path is acting weird
    path("search", views.search, name="search"),
    path("<str:title>", views.entry, name="entry"),
]
