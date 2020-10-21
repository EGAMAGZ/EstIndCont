from django.urls import path

from .views import UnityContentView, UnityListContent

urlpatterns = [
    path('', UnityListContent.as_view(), name='unity-content-list'),
    path('<slug:topic_slug>/', UnityContentView.as_view(), name='unity-content')
]
