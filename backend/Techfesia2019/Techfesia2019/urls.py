"""Techfesia2019 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title="Techfesia2019 API")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs', schema_view),
    path('auth/', include("registration.urls")),
    path('users/<str:username>/invitations/', include('event_registrations.invitation_urls')),
    path('events/<str:public_id>/registrations/', include('event_registrations.event_registration_urls')),
    path('users/', include("accounts.urls")),
    path('teams/', include('event_registrations.team_urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
    path('csv/', include('event_registrations.csv_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
