from django.urls import path
from .views import TeamDetailView, TeamListView

urlpatterns = [
    path('<slug:public_id>/', TeamDetailView.as_view()),
    path('', TeamListView.as_view())
]
