
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('createOrder/', views.createOrder.as_view()),
    path('orderDetails/', views.getOrderDetails.as_view()),
    path('updateOrder/', views.updateOrder.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)