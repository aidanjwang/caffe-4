from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Homepage.")


def create_order(request):
    if request.method == "GET":
        return render(request, 'create-order.html')
    else:
        return HttpResponse("Post request.")
