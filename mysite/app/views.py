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
        # would use API here
        if link == "insert link":
            name = ""
            picture = ""
            asin = ""
            units = 0
            price = 0
        mega_order = MegaOrder(name=name, )
        mega_order.save()
        return redirect()


def order_details(request):
    if request.method == "GET":
        return render(request, 'order-details.html')
    else:
        order = request.POST['order']
        name = request.POST['name']
        email = request.POST['email']
        units = request.POST['units']
        mini_order = MiniOrder(order=order, name=name, email=email, units=units)
        mini_order.save()
        check_order()
        return render(request, 'complete-order.html')


def check_order():
    return HttpResponse("Check order") # TODO

