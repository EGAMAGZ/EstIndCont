from django.urls import path

from .views import UnityList

urlpatterns = [
    path('', UnityList.as_view())
]
