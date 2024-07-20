import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Embed
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("Token not found. Make sure the .env file is correctly set up.")
    exit()

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

ALLOWED_CHANNEL_ID = 1017448272006217834

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    # Register slash commands if they are not automatically registered
    for cog in bot.cogs.values():
        if hasattr(cog, 'register_commands'):
            await cog.register_commands()

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.slash_command(name="triggermaker", description="Generate a TriggerServerEvent command")
async def triggermaker(interaction: Interaction, input1: str, input2: str):
    if interaction.channel.id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message("You can only use this command in the specified channel.", ephemeral=True)
        return

    input1 = input1.replace('[', '').replace(']', '')
    input2 = input2.replace('[', '').replace(']', '')

    embed = Embed(title="هذا الترقر الي تبيه", description="PSYCHO IS HERE BETCH\n\nHere is your command:", color=0x00ff00)
    embed.add_field(name="You Entered", value=f"```{input1}```\n\n```{input2}```", inline=False)
    embed.add_field(name="Final Output", value=f"```TriggerServerEvent(\"{input1}\", {input2})```", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/880044525190533171/1263761958587469906/a_7d5220031241a4617f1815f5eab5de62.gif?ex=669b698a&is=669a180a&hm=cfd0c9efdfd7c5d5fc2bea5abdd0aefd0c76e3ab6d4964dfb73bac60c5d5d4cc&")

    await interaction.response.send_message(embed=embed, ephemeral=True)

    user = interaction.user
    try:
        dm_channel = await user.create_dm()
        await dm_channel.send(embed=embed)
    except Exception as e:
        print(f"An error occurred while sending DM: {e}")

from keep_alive import keep_alive
keep_alive()

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"An error occurred: {e}")