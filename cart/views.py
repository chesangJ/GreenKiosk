from django.shortcuts import render, redirect

import orders
from orders.form import OrderUploadForm
import payment
from .models import Cart
from inventory.models import Product

def cart_detail(request):
    user_cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'user_cart': user_cart})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product.name,
        defaults={'price': product.price, 'quantity': 1, 'image': product.image}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(pk=cart_item_id, user=request.user)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart_detail')

def checkout(request):
    if request.method == "POST":
        # Validate the checkout form
        form = OrderUploadForm(request.POST)
        if form.is_valid():
            # Process the payment
            payment.process_payment(form.cleaned_data)

            # Create an order
            order = orders.objects.create(
                customer=request.user,
                shipping_address=form.cleaned_data["shipping_address"],
                billing_address=form.cleaned_data["billing_address"],
                payment_details=form.cleaned_data["payment_details"],
            )

            # Redirect to the confirmation page
            return redirect("checkout_success")

    else:
        # Render the checkout form
        return render(request, "cart/checkout.html", {"form": OrderUploadForm()})
 





