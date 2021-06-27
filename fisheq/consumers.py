import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class FishingConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        
        await self.send({
            "type": "websocket.accept"
        })

    async def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )