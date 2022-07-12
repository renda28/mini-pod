from django.urls import path

from api.models import Room
from .views import RoomView

urlpatterns = [
    path('', RoomView.as_view()),
]
