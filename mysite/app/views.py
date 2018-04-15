from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def create_order(request):
    if request.method == "GET":
        return render(request, 'create-order.html')
    else:
        return HttpResponse("Post request.") # TODO


def order_details(request):
    if request.method == "GET":
        return HttpResponse("Get request.") # TODO
    else:
        return HttpResponse("Post request.") # TODO


def finish_order():
    return HttpResponse("Finish order") # TODO

