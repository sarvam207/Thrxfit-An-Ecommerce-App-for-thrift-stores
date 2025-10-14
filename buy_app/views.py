from django.shortcuts import render

# Create your views here.
def buy_success(request):
    return render(request, 'buy_app/buy_success.html')


def buy_failed(request):
    return render(request, 'buy_app/buy_failed.html')


def checkout(request):
    
    return render(request, 'buy_app/checkout.html')