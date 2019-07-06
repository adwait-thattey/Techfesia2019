from django.urls import path
from .views import EventRegistrationView, EventRegistrationDetailView, EventRegistrationListView

urlpatterns = [
    path('', EventRegistrationView.as_view()),
    path('view/', EventRegistrationDetailView.as_view()),
    path('view_all/', EventRegistrationListView.as_view()),
]
