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
    if util.get_entry(f"title") == None:
        return render(request, "encyclopedia/notFound.html")
    # this is what will render if the entry exists
    return render(request, "encyclopedia/entries.html", {
        "title": markdowner.convert(util.get_entry(f"{title}"))
    })

class NewEntryForm(forms.Form): # a form to create a new entry
    title = forms.CharField(label = "Title")
    entry = forms.CharField(label = "Entry") #change this to a textarea

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            entry = form.cleaned_data["entry"]
            util.save_entry(f"{title}", f"{entry}")
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
            ##
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })