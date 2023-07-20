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
        "title": markdowner.convert(util.get_entry(f"{title}"))
    })

class NewEntryForm(forms.Form): # a form to create a new entry
    title = forms.CharField(label = "Title")#change this to a textarea
    # a workaround. Without the entry variable, the new function does not work, traceback error to 'entry = form.cleaned_data["entry"]'
    entry = forms.CharField(widget = forms.HiddenInput(), required=False)

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
            
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

def search(request, query):

    entries = util.list_entries()
    markdowner = Markdown()
    print(entries)

    for item in entries:
        if query == item:
            print(query)
            return render(request, "encyclopedia/entries.html", {
                "title": markdowner.convert(util.get_entry(f"{query}"))
            })
        elif item.__contains__(f"{query}"):

            return render(request, "encyclopedia/search.html", {
                "match_result": item
            })

            print(item)
            return HttpResponse(item)