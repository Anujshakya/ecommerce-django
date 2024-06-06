from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView, HomeView,SearchResultsView, ProductCategoryListView

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product_list'),
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_products'),
    path('category/<product_category>/', ProductCategoryListView.as_view(), name="filter"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)