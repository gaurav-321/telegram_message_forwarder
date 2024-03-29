import json

from telethon import TelegramClient, events, types
from telethon.tl.functions.messages import SendMediaRequest

# Your API credentials
from telethon.tl.types import InputPeerChat
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

# Your phone number (include the country code)
phone_number = os.getenv('phone_number')
forward_group = os.getenv('forward_group')
channels = os.getenv('channels').split(',')


async def send_msg(client, data, group_id=forward_group):
    chat_entity = InputPeerChat(group_id)
    await client.send_message(chat_entity, data)


with TelegramClient('name', api_id, api_hash) as client:
    client.parse_mode = 'html'


    @client.on(events.NewMessage)
    async def handler(event):
        message = event.message.to_dict()
        # print(message)
        if message['peer_id']['channel_id'] in channels:
            urls = []
            print(message['message'], message['peer_id']['channel_id'])
            for entity in message['entities']:
                if "url" in entity.keys():
                    urls.append(entity['url'])
            print(urls)
            await send_msg(client, message['message'])


    client.run_until_disconnected()
