import discord
from discord.ext import commands
prefixint = "n!"

class Game(commands.Cog):
    
    def __init__(self, client):
        self.client = client 
        
def setup(client):
    client.add_cog(Game(client))