from django.http import HttpResponse
from django.shortcuts import render, redirect
from mysite.app.models import MegaOrder, MiniOrder


def home(request):
    return render(request, 'home.html')


def create_order(request):
    if request.method == "GET":
        return render(request, 'create-order.html')
    else:
        link = request.POST['link']
        # would use API
        if link == "insert link":
            name = ""
            picture = ""
            asin = ""
            units = 0
            price = 0
        megaOrder = MegaOrder(name=name, )
        megaOrder.save()
        return redirect()

def order_details(request):
    if request.method == "GET":
        return render(request, 'order-details.html')
    else:
        return HttpResponse("Post request.") # TODO


def finish_order():
    return HttpResponse("Finish order") # TODO

