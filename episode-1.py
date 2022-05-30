import discord 
from discord import app_commands
from typing import Optional

from pyparsing import Opt


MY_GUILD = discord.Object(id=979989331919904768) # replace with your guild ID


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, application_id: int):
        super().__init__(intents=intents, application_id=application_id)


        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)



intents = discord.Intents.all()

client = MyClient(intents=intents, application_id=980012443277344809) # replace with your bot's ID

@client.event
async def on_ready():
    print(f"Logged in as {client.user}\nUser id: {client.user.id}")



@client.tree.command(name="slash-command")
async def slash(interaction: discord.Interaction, additional_text: Optional[str]):
    embed = discord.Embed(title=f"How to do slash commands with {interaction.user.name}")
    embed.add_field(name="Your text was:", value=additional_text)
    await interaction.response.send_message(embed=embed, ephemeral=True)

client.run("")
