from django.urls import path
from .views import initiate_payment, callback, PaymentInitiateView

urlpatterns = [
    # path('initiate', initiate_payment, name='pay'),
    path('initiate', PaymentInitiateView.as_view(), name='payment_initiate'),
    path('callback/', callback, name='callback'),
]
