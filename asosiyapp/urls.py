from django.urls import path
from .views import *

urlpatterns = [
    path('bolim/', BolimView.as_view(), name='bolim'),
    path('mahsulotlar/', ProductView.as_view(), name='mahsulotlar'),
    path('product_edit/<int:pk>/', ProductEditView.as_view(), name='product_edit'),
    path('clients/', ClientView.as_view(), name='clients'),
    path('client_edit/<int:pk>/', ClientEditView.as_view(), name='client_edit'),
]
