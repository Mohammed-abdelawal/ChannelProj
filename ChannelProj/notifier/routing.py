from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/chat/<str:room_name>',WSConsumer.as_asgi()),

]