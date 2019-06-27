from django.urls import path
from .views import TeamDetailView

urlpatterns = [
    path('<slug:public_id>/', TeamDetailView.as_view()),
]
