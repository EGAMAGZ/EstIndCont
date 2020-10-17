from django.urls import path

from .views import unity_list_content,unity_content

urlpatterns = [
    path('', unity_list_content, name='unity-content-list'),
    path('<slug:topic_slug>/', unity_content, name='unity-content')
]
