import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

class PublicChatConsumer(AsyncWebsocketConsumer): 
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_name'] # /ws/chat/brawlstart/ room_name = 'brawlstars'
        print(self.room_name)
        self.room_group_name = f'chat_{self.room_name}' # room_group_name = 'chat_brawlstars' 
        print(self.channel_name) 

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message
            }
            )
        
        
    async def chat_message(self, event):
        message = event['message']
        print('chat_message')
        print(message)
        await self.send(text_data=json.dumps({
            'message': message,
        }))