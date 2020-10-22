from django.urls import path

from .views import UnityList, TeamMembersList

urlpatterns = [
    path('', UnityList.as_view()),
    path('team/', TeamMembersList.as_view(), name='team-members')
]
