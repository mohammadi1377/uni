from django.urls import path
from .api_views import RegisterView

app_name = 'api'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]