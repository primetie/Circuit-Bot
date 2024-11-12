import discord

class Client(dicord.Client):
    async def on_ready(self):
        print('Logged on as {self.user}!')
        
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run()

