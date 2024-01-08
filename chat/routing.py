from django.urls import path, re_path
from .consumers import PublicChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_name>\w+)/$', PublicChatConsumer.as_asgi()),
]