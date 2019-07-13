from django.urls import path
from .views import EventRegistrationView, EventRegistrationDetailView, EventRegistrationListView

urlpatterns = [
    path('', EventRegistrationView.as_view(), name='create_event_registration'),
    path('view', EventRegistrationDetailView.as_view(), name='event_registration_detail'),
    path('view_all', EventRegistrationListView.as_view(), name='list_event_registration'),
]
