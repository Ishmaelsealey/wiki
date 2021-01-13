from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markdowner = Markdown()
    return render(request, "encyclopedia/entries.html", {
        "title": markdowner.convert(util.get_entry(f"{title}"))
    })
