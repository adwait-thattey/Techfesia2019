from django.urls import path
from .views import TeamEventRegistrationView, TeamEventRegistrationDetailView, TeamEventRegistrationListView

urlpatterns = [
    path('', TeamEventRegistrationView.as_view()),
    path('view/', TeamEventRegistrationDetailView.as_view()),
    path('view_all/', TeamEventRegistrationListView.as_view()),
]
