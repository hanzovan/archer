from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewItemForm(forms.Form):
    item = forms.CharField(label="item's name")

# Create your views here.
def index(request):
    if "items" not in request.session:
        request.session["items"] = []

    return render(request, "inventory/index.html", {
        "items": request.session["items"]
    })

def add(request):
    # Add item to the list

    # If user reached route via submitting form:
    if request.method == "POST":

        # get the form input from the browser
        form = NewItemForm(request.POST)

        # If form is valid, get the information which include "item"
        if form.is_valid():
            item = form.cleaned_data["item"]

            # Add item to the list
            request.session["items"] += [item]
            return HttpResponseRedirect(reverse("inventory:index"))

        # If form is not valid, display a new form
        else:
            return render(request, "inventory/add.html", {
                "form": form
            })


    else:
        return render(request, "inventory/add.html", {
            "form": NewItemForm
        })