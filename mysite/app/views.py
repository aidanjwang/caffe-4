from django.http import HttpResponse


def home(request):
    return HttpResponse("Homepage.")


def create_order(request):
    return HttpResponse("Create order.")
