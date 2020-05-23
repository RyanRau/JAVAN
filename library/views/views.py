from django.shortcuts import render


# .../library
def index(request):
    context = {

    }
    return render(request, "./library/index.html", context)
