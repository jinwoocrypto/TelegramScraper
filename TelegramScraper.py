from telethon import TelegramClient, events

#➤𝐕𝐨𝐫𝐭𝐞𝐱 𝐍𝐞𝐭𝐰𝐨𝐫𝐤™
#➤𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : https://t.me/VorTexNetworkTeam
#➤𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 𝐓𝐞𝐚𝐦 : https://t.me/VorTexNetworkTeam
#➤𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : https://t.me/VorTexNetworkTeam

api_id = ''
api_hash = ''

# Channels and groups to monitor (assuming these are the public usernames):
channels_to_monitor = [
    '@OficialScorpionsGrupo',
    '@PremiumBinsStore',
]

#ADD HOW MUCH YOU WANT CHEDK I ADDED SOME GROUPS HERE YOU CAN ADD MORE

destination_channel_username = '@privateScrapers'  # Replace with the actual username of your destination channel

#ADD YOUR CHANNEL USERNAME HERE WHERE YOU WANT TO FORWARD THE APPROVED

approval_patterns = [
    '𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅',
    '𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved ✅',
    'Status ➜ ϟ Approved! ✅',
    'Message ➜ ϟ succeeded',
    'Status -» Approved! ✅'
]
#HOW MUCH YOU WANT LINE BY LINES
with TelegramClient('anon', api_id, api_hash) as client:
    
    @client.on(events.NewMessage(chats=channels_to_monitor))
    async def new_message_handler(event):
        for pattern in approval_patterns:
            if pattern in event.message.text:
                await event.message.forward_to(destination_channel_username)
                break

    @client.on(events.MessageEdited(chats=channels_to_monitor))
    async def edited_message_handler(event):
        for pattern in approval_patterns:
            if pattern in event.message.text:
                await event.message.forward_to(destination_channel_username)
                break

    client.run_until_disconnected()
