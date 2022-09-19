from django.shortcuts import render


items = ["phone", "tv", "table"]
# Create your views here.
def index(request):
    return render(request, "inventory/index.html", {
        "items": items
    })

