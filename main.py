import discord
import os
token = os.environ['token']

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        print(message.channel)
        if message.author == self.user:
            return
        logs = client.get_channel(1305980871127601244)
        await logs.send(f'{message.author} said {message.content}')
        
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(token)

