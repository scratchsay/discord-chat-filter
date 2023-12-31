import discord
from better_profanity import profanity
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
profanity.load_censor_words()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = 'channels and reports.'))
    print("Bot loaded!")

@client.command()
async def SRL(ctx):
    await ctx.send("Stop Rude Language v.1.0.0")

@client.event
async def on_message(message):
    if not message.author.bot:
        censored_text = profanity.censor(message.content)
        if censored_text != message.content:
            await message.channel.send(f"{message.author.mention} Please do not use profanity.")

@client.event
async def on_message_edit(before, after):
    censored_text = profanity.censor(after.content)
    print(censored_text)
    if censored_text != after.content:
        await after.channel.send(f"{after.author.mention} Please do not use profanity.")

client.run(token)
