from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

from users.models import CustomUser
from products.models import Product
from .models import Cart, Order

# Create your views here.
class AddToCartView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        customUser, created = CustomUser.objects.get_or_create(username = self.request.user)
        cart_item, created = Cart.objects.get_or_create(customUser=customUser, product=product)
        
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        
        referer= request.META.get('HTTP_REFERER', '/')
        return redirect(referer)
        # return JsonResponse({'status': 'success', 'message': 'Item added to cart'})
    
class CartDetailView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart_detail.html'
    login_url = 'login'
    context_object_name = 'cart_items'
    
    def get_queryset(self):
        return Cart.objects.filter(customUser=self.request.user)
    
class CheckOutView(LoginRequiredMixin, View):
    login_url = 'login'
    success_url = reverse_lazy('order_detail')
    
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(customUser=self.request.user)
        
        # order = Order.objects.get(user=self.request.user)
        
        for item in cart:
            Order.objects.create(customUser=item.customUser, product=item.product, quantity=item.quantity)
            
        cart.delete()
        
        return redirect(self.success_url)
    
class OrderDetailView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_detail.html'
    login_url = 'login'
    context_object_name = 'order_items'
    
    def get_queryset(self):
        return Order.objects.filter(customUser=self.request.user)
    
    
# @method_decorator(login_required, name='dispatch')
class CartView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        cart = Cart.objects.filter(customUser=self.request.user)
        context = {'cart': cart}
        return render(request, 'cart_detail.html', context)

    def post(self, request):
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        cart = Cart.objects.filter(customUser=self.request.user)

        if action == 'increment':
            cart_item = cart.get(product_id=product_id)
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'decrement':
            cart_item = cart.get(product_id=product_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        elif action == 'delete':
            cart_item = cart.get(product_id=product_id)
            cart_item.delete()

        return redirect('cart_detail')