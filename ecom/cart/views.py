from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse




def cart_summary(request):
    return render(request, 'cart_summary.html', {
        
    })


def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        
        product_id = int(request.POST.get('product_id'))
        
        product = get_object_or_404(Product, id=product_id)
        
        #Saving to our session
        cart.add(product=product)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        #Returning response
        response = JsonResponse({'qty ': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
