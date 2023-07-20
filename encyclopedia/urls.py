from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new, name="new"),
    path("<str:title>", views.entry, name="entry"),
    # query path is acting weird
    path("query", views.search, name="search"),
]
