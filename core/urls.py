from django.urls import path

from .views import TeamMembersList, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('team/', TeamMembersList.as_view(), name='team-members')
]
