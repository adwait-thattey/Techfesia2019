from django.urls import path
from .views import TicketCreateListView

urlpatterns = [
    path('ticket', TicketCreateListView.as_view()),
    # path('ticket/<str:public_id>/',)
]
