from django.http import HttpResponse
from django.shortcuts import render, redirect
# from mysite.app.models import MegaOrder, MiniOrder
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def create_order(request):
    if request.method == "GET":
        return render(request, 'create-order.html')
    else:
        itemurl = request.POST['itemurl']
        # would use API
        if itemurl == "https://www.amazon.com/Cannery-Row-Centennial-John-Steinbeck/dp/014200068X/":
            name = "Cannery Row: (Centennial Edition) Paperback – Deckle Edge, February 5, 2002"
            picture = "https://images-na.ssl-images-amazon.com/images/I/51pKtoV%2Bd2L._SX332_BO1,204,203,200_.jpg"
            asin = "014200068X"
            units = 0
            price = 13.89
        # megaOrder = MegaOrder(name=name, )
        # megaOrder.save()
        # return redirect("", )
        # url = reverse('app/order-details', kwargs={'name': name, 'picture': picture, 'price': price})
        # return HttpResponseRedirect(url)
        return render(request, 'order-details.html')
    # template = loader.get_template("app/order-details.html")
    # context = {'name': name; 'picture': picture; 'price': price}
    # return redirect(template.render(context, request))
    

def order_details(request):
    if request.method == "GET":
        return render(request, 'order-details.html')
    else:
        return HttpResponse("Post request.") # TODO


def finish_order():
    return HttpResponse("Finish order") # TODO

