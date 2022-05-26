
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('products/<int:pgno>', views.getProductsList.as_view()),
    path('createProduct/', views.createProduct.as_view()),
    path('productDetails/<int:pk>/', views.getProductDetails.as_view()),
    path('updateProduct/<int:pk>/', views.updateProduct.as_view()),
    path('deleteProduct/<int:pk>/', views.deleteProduct.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)