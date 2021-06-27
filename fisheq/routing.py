from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/team(?P<room_code>[\w.@+-]+)(?P<tn>[\w.@+-]+)', consumers.FishingConsumer.as_asgi()),
]