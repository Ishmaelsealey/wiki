from django.urls import path
import random
from . import views, util

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new, name="new"),
    path("random", views.randomEntry, name="random"),
    path("<str:title>", views.entry, name="entry"),
    # query path is acting weird
    path("query", views.search, name="search"),
]
