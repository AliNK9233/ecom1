from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Cart
from user_app.models import Address
from .models import Order


# Create your views here.

def order_list(request):
    # Retrieve all orders
    orders = Order.objects.all()

    context = {
        'orders': orders
    }

    return render(request, 'orders/order_list.html', context)

def checkout(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    addresses = Address.objects.filter(user=user)
    
    # Assume you have a list of predefined payment types
    payment_types = ['Credit Card', 'Cash on Delivery', 'UPI']

    if request.method == 'POST':
        # Process form submission and create an order
        shipping_address_id = request.POST.get('shipping_address')
        payment_type = request.POST.get('payment_type')

        if shipping_address_id and payment_type:
            shipping_address = Address.objects.get(id=shipping_address_id)

            order = Order.objects.create(
                user=user,
                total_price=cart.total_price,
                payment_status='Pending',
                delivery_status='Pending',
                payment_type=payment_type,
                shipping_address=shipping_address,
            )

            order.items.set(cart.items.all())

            # Clear the cart after creating the order
            cart.items.clear()
            cart.total_price = 0
            cart.save()

            return render(request, 'orders/thank_you_page.html', {'order': order})

    return render(request, 'orders/checkout.html', {'cart_items': cart.items.all(), 'total_price': cart.total_price, 'addresses': addresses, 'payment_types': payment_types})

def order_tracking(request, order_id):
    addresses = Address.objects.filter(user=request.user)
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_tracking.html', {'order': order, 'addresses': addresses})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.delivery_status == 'Pending':
        # Implement your cancellation logic here
        order.delivery_status = 'Cancelled'
        order.save()
        return redirect('order_tracking', order_id=order_id)
    else:
        return redirect('order_tracking', order_id=order_id)

def change_address(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.delivery_status == 'Pending':
        if request.method == 'POST':
            new_address_text = request.POST.get('new_address')
            # Implement your logic to update the address here
            new_address = Address.objects.create(user=order.user, street_address=new_address_text, city='YourCity', state='YourState', zip_code='YourZipCode')
            order.shipping_address = new_address
            order.save()

        return redirect('order_tracking', order_id=order_id)
    else:
        return redirect('order_tracking', order_id=order_id)
    


   