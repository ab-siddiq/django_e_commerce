from django.shortcuts import render

# Create your views here.
def order_completed(request):
    return render(request,'orders/order_complete.html')
def place_order(request):
    return render(request,'orders/place_order.html')