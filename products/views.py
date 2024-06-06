from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q

from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    
    
class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = "category_list"
    
    def get_queryset(self):
        categories = Product.objects.values('category').distinct()
        categories_with_images = []

        for category in categories:
            product_with_image = Product.objects.filter(category=category['category']).first()
            if product_with_image:
                categories_with_images.append({
                    'category': category['category'],
                    'image': product_with_image.image
                })
        return categories_with_images
    
    
class SearchResultsView(ListView):
    model = Product
    template_name = "search_list.html"
    context_object_name = "searched_results"
    
    def get_queryset(self):
        query = self.request.GET.get("searched_product")
        searched_results = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        return searched_results
    
    
class ProductCategoryListView(ListView):
    model = Product
    template_name = 'category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        product_category = self.kwargs['product_category']
        return Product.objects.filter(category=product_category)