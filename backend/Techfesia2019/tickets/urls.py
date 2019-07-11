from django.urls import path
from .views import TicketCreateListView, TicketCloseView, PublicTicketListView, TicketCommentDetailUpdateDeleteView
from .views import TicketCommentListCreateView, TicketSubscribeView, TicketUnsubscribeView, TicketDetailView

urlpatterns = [
    path('', TicketCreateListView.as_view(), name='tickets_list_staff_create_user'),
    path('public/', PublicTicketListView.as_view(), name='tickets_list_public'),
    path('<str:username>/', TicketCreateListView.as_view(), name='ticket_list'),
    path('<str:public_id>/detail/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<str:public_id>/close/', TicketCloseView.as_view(), name='ticket_close'),
    path('<str:public_id>/subscribe/', TicketSubscribeView.as_view(), name='ticket_subscribe'),
    path('<str:public_id>/unsubscribe/', TicketUnsubscribeView.as_view(), name='ticket_unsubscribe'),
    path('<str:public_id>/comment/', TicketCommentListCreateView.as_view(), name='ticket_comment_create_list'),
    path('<str:public_id>/comment/<str:comment_id>/', TicketCommentDetailUpdateDeleteView.as_view(),
         name='ticket_comment_detail'),
]
