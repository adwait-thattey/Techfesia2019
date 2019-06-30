from django.urls import path
from .views import TicketCreateListView, TicketCloseView, PublicTicketListView, TicketCommentDetailUpdateDeleteView
from .views import TicketCommentListCreateView

urlpatterns = [
    path('', TicketCreateListView.as_view()),
    path('public/', PublicTicketListView.as_view()),
    path('<str:username>/', TicketCreateListView.as_view()),
    path('<str:public_id>/close/', TicketCloseView.as_view()),
    path('<str:public_id>/comment/', TicketCommentListCreateView.as_view()),
    path('<str:public_id>/comment/<str:comment_id>/', TicketCommentDetailUpdateDeleteView.as_view()),
]
