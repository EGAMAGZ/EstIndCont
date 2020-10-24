from django.urls import path

from .views import UnityList, TeamMembersList

urlpatterns = [
    path('', UnityList.as_view(), name='home'),
    path('team/', TeamMembersList.as_view(), name='team-members')
]
