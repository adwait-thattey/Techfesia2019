from django.urls import path
from .views import EventsListView, EventModifyView
from .views import VolunteerListView, VolunteerDetailView

urlpatterns = [
    # Event Paths
    path('', EventsListView.as_view(), name='events_list'),
    # path('<int:pk>/register/', EventRegisterView.as_view(), name='event_register'),
    path('<int:pk>/', EventModifyView.as_view(), name='event_modify'),

    # Volunteer Paths
    path('volunteers/', VolunteerListView.as_view(), name='volunteer_list'),
    path('volunteers/<int:pk>/', VolunteerDetailView.as_view(), name='volunteer_detail'),
]
