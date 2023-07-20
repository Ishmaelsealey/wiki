from django.urls import path
import random
from . import views, util
# allEntries = util.list_entries()

def randomEntry():
    allEntries = util.list_entries()
    return random.choice(allEntries)

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.new, name="new"),
    path("<str:title>", views.entry, name="entry"),
    # query path is acting weird
    path("query", views.search, name="search"),
    # path(f"{random.choice(allEntries)}", views.entry, name="random")
    path(f"{randomEntry()}", views.entry, name="random")
]
