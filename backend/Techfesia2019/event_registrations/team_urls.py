from django.urls import path
from .views import TeamDetailDeleteView, TeamListCreateView

urlpatterns = [
    path('<slug:public_id>/', TeamDetailDeleteView.as_view(), name='team_details'),
    path('', TeamListCreateView.as_view(), name='teams_list'),
]
