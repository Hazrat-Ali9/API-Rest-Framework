from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductsAPIView.as_view(), name='products_api'),
    path('api/category/<slug:category_slug>/', views.ProductsAPIView.as_view(), name='products_by_category_api'),
    path('api/add_product/', views.add_product_api, name='add_product_api'),
    path('api/products/<int:product_id>/', views.update_product_api, name='update_product_api'),
    path('api/products/<int:product_id>/delete/', views.delete_product_api, name='delete_product_api'),
]

