from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request): # Returns a list of entries
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })  

def entry(request, title):  # gets the entry
    markdowner = Markdown()
    # if statement required to check if the entry exists
    if util.get_entry(f"{title}") == None:
        return render(request, "encyclopedia/notFound.html")
    # this is what will render if the entry exists
    return render(request, "encyclopedia/entries.html", {
        "title": markdowner.convert(util.get_entry(f"{title}")),
        "entryTitle": title
    })

class NewEntryForm(forms.Form): # a form to create a new entry
    title = forms.CharField(label = "Title")
    entry = forms.CharField(widget=forms.Textarea, label = "Entry")

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]
            if util.get_entry(f"{title}") == None:
                util.save_entry(f"{title}", f"{entry}")
                return HttpResponseRedirect(reverse("encyclopedia:index"))
            else:
                return render(request, "encyclopedia/entryExists.html", {
                    "title": title
                })
        else:
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
            
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

import random
# Get a random entry from the list of entries
# Go to the path with the entry's title

def randomEntry(request):
    markdowner = Markdown()
    allEntries = util.list_entries()
    chosen = random.choice(allEntries)
    return render(request, "encyclopedia/entries.html", {
        "title": markdowner.convert(util.get_entry(f"{chosen}"))
    })

def search(request):
    query = request.GET.get("q")
    entryList = util.list_entries()
    markdowner = Markdown()
    matchingResults = []

    # This works if entry is exact match!
    for item in entryList:
        if query == item:
            return render(request, "encyclopedia/entries.html", {
                "title": markdowner.convert(util.get_entry(f"{query}"))
            })
    #This works!
        elif item.__contains__(f"{query}"):
            matchingResults.append(item)
    return render(request, "encyclopedia/search.html", {
        "match_result": matchingResults
    })

def edit(request, title):
    entryBody = util.get_entry(f"{title}")
    class editEntryForm(forms.Form):
        entryText = forms.CharField(widget=forms.Textarea, label="Edit Entry", initial=f"{entryBody}")
    if request.method == "POST":
        form = editEntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entryText"]
            util.save_entry(f"{title}", f"{entry}")
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "form": editEntryForm()
        })