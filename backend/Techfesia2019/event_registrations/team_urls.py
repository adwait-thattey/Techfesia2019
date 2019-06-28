from django.urls import path
from .views import TeamDetailEditDeleteView, TeamListCreateView

urlpatterns = [
    path('<slug:public_id>/', TeamDetailEditDeleteView.as_view(), name='team_details'),
    path('', TeamListCreateView.as_view(), name='teams_list'),
]
