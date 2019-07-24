from django.urls import path
# from .views import callback
from .views import PaymentInitiateView, PaytmCallbackView

urlpatterns = [
    path('initiate', PaymentInitiateView.as_view(), name='payment_initiate'),
    path('callback/', PaytmCallbackView.as_view(), name='callback'),
    # path('callback/', callback, name='callback'),
]
