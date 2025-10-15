from django.shortcuts import render
from . models import BuyAddress, OrderItem, Order
from cart_app.cart import Cart
from django.http import JsonResponse



# Create your views here.
def buy_success(request):
    
    for key in list(request.session.keys()):
        if key == 'cart':
            del request.session[key]
            
    return render(request, 'buy_app/buy_success.html')


def buy_failed(request):
    return render(request, 'buy_app/buy_failed.html')


def checkout(request):
    
    if request.user.is_authenticated:
        try:
            shipping_address = BuyAddress.objects.get(user=request.user.id)
            context={'shipping':shipping_address}
            return render(request, 'buy_app/checkout.html', context)
        except:
            return render(request, 'buy_app/checkout.html')
    else:
        return render(request, 'buy_app/checkout.html')
    
def complete_order(request):
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        shipping_address = (address + "\n" + city + "\n" + state + "\n" + zipcode   )

        
        cart = Cart(request)
        total_cost = cart.get_total()
        
        '''
        order variations:
        1. create order -> account user with or without saved address
        2. create order -> guest user
        
        '''
        
        if request.user.is_authenticated:
            order = Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=address,
                amount_paid=total_cost,
                user=request.user
                )
            order_id = order.pk
            
            for item in cart:
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    user=request.user,
                )
    
        else:
            order = Order.objects.create(
                full_name=name,
                email=email,
                phone=phone,
                shipping_address=shipping_address,
                amount_paid=total_cost,
                )
            order_id = order.pk
            
            for item in cart:
                OrderItem.objects.create(
                    order_id=order_id,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                    )
        order_success = True
        response = JsonResponse({'success': order_success})
        
    
        return response




