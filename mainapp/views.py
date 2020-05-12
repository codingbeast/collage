from django.shortcuts import render
from django.shortcuts import reverse
from iptools import views
def homepage(request):
    iplink=reverse("iptools:home")
    wordranker=reverse("wordranker:frenq")
    context={
        "ip": iplink,
        "wordranker": wordranker,
    }
    return render(request,"index.html",context)
