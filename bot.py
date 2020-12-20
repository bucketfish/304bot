import os
import discord

import random

from dotenv import load_dotenv
from discord.ext import commands

from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='~')
bot.remove_command("help")

error = ("sorry, couldn't understand")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('with 304\'20! | ~help'))

@bot.command(name="ping")
async def pingpong(ctx):
    try:
        response = "pong, " + ctx.author.nick +"!"
    except:
        response = "pong, " + ctx.author.name +"!"

    await ctx.send(response)

@bot.command(name="help")
async def help(ctx):
    await ctx.send("""
> hello! i'm your local class 304 discord bot. i send things!
> unfortunately the help menu isn't very well documented since i can't do anything yet.
> hopefully this will change!
> prefix: `~`

> current commands:
> - `help` to show this page!
> - `ping` to test if the bot is online
> - `alphabet` to show the gay alphabet

> i also sometime respond to messages ^^
    """)

@bot.command(name="alphabet")
async def alphabet(ctx):
    await ctx.send("""
_**__THE GAY ALPHABET__**_
a for ace-icles
b for biangle
c for cricle
d for diffany
e for elmo
f for press f to pay respecc
g for girl in red
h for homo sapien
i for i'm gay
j for joella
k for keysmahingresdftyguhijougft
l for love, simon
m for minecraft
n for nonbinary
o for oreo
p for pride
q for queerkiwi
r for rick astley
s for ssssssssssimp
t for trans rights
u for unable to math
v for void
w for wickwoll uwu >.<
x for xzswerdtfyguhijlouytrse
y for yeehaw
z for zzzz
    """)

@bot.command('test')
async def test(ctx):
    if ctx.author.id == 670962000964354049:
        await ctx.send("tongyu testing")

@bot.event
async def on_member_join(member):
    await bot.get_channel(788726154269294635).send("welcome to 304's class discord server, " + member.mention + "! i'm your local 304 class bot :D hope you enjoy your time here! do send an intro in " + bot.get_channel(788772685131415602).mention + ".")

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    if 'happy birthday' in ctx.content.lower():
        await ctx.channel.send('happy birthday!🎈🎉')

    if 'aro' in ctx.content.lower():
        thing = random.randint(0, 10)
        if thing == 0:
            await ctx.channel.send('aromatic 🕯')
        elif thing == 1:
            await ctx.channel.send('aerodynamic aros')
        elif thing == 2:
            await ctx.channel.send('why ship when you can aro-plane people?')
        elif thing == 3:
            await ctx.channel.send('two aros sitting in a tree \n s-i-t-t-i-n-g')
        elif thing == 4:
            await ctx.channel.send('🏹 a r r o w')
        elif thing == 5:
            await ctx.channel.send('aro rights!')

    if 'gay' in ctx.content.lower():
        thing = random.randint(0, 10)
        if thing == 0:
            await ctx.channel.send('GAYYYYYYYYY')
        elif thing == 1:
            await ctx.channel.send('gay rights babey!')
        elif thing == 2:
            await ctx.channel.send('let\'s go gaymers')
        elif thing == 3:
            await ctx.channel.send('🥳🎉🏳️‍🌈')
        elif thing == 4:
            await ctx.channel.send('e is for elmo')
        elif thing == 5:
            await ctx.channel.send('hi this is 304 bot um sorry for disturbing but i think i\'m, uh, coming out as gay! yee')
        elif thing == 6:
            await ctx.channel.send('i am a secret gaygent and i\'m spying shh')

    if 'ace' in ctx.content.lower():
        thing = random.randint(0, 10)
        if thing == 0:
            await ctx.channel.send('i aced my bot exams to become a real bot :D')
        elif thing == 1:
            await ctx.channel.send("welcome to ace hardware there's no screwing just tons of screws")
        elif thing == 2:
            await ctx.channel.send('ACE-OLOTL!!')
        elif thing == 3:
            await ctx.channel.send('||wait... if i\'m ace and you\'re ace who gives a fuck?||')
        elif thing == 4:
            await ctx.channel.send('instead of coming out of the closet i came out of the deck!! :D')
        elif thing == 5:
            await ctx.channel.send("please don't hug asexuals you gotta embr**ace** them")

    if 'bi' in ctx.content.lower():
        thing = random.randint(0, 10)
        if thing == 0:
            await ctx.channel.send('bisexuals are   werewolves confirmed')
        elif thing == 1:
            await ctx.channel.send("a bisexual witch call that a bihexual")
        elif thing == 2:
            await ctx.channel.send('ways to attract a bisexual: make lots of bi puns')
        elif thing == 3:
            await ctx.channel.send('bi-derman bi-derman')
        elif thing == 4:
            await ctx.channel.send('hey all my bi babies out there please check your posture')
        elif thing == 5:
            await ctx.channel.send("pray for all the bisexual's ankles during this cold time😔")

    if 'haiku bot' in ctx.content.lower() or 'haikubot' in ctx.content.lower() or 'haiku' in ctx.content.lower():
        thing = random.randint(0, 3)
        if thing == 0:
            await ctx.channel.send('... did someone mention haikubot?')
        if thing == 1:
            await ctx.channel.send("you're so mean to haiku baby😤")
        if thing == 2:
            await ctx.channel.send('haiku bot :O')
        if thing == 3:
            await ctx.channel.send('i hate haikubot too')

    if '304 bot' in ctx.content.lower():
        thing = random.randint(0, 6)
        if thing == 0:
            await ctx.channel.send('did someone call me?')
        elif thing == 1:
            await ctx.channel.send('is anyone talking about me behind my back 👀')
        elif thing == 2:
            await ctx.channel.send('love me take me kiss me get me closer!')
        elif thing == 3:
            await ctx.channel.send('you called?')
    
    elif '304' in ctx.content.lower():
        thing = random.randint(0, 5)
        if thing == 0:
            await ctx.channel.send('i LOVE 304!!! <333')
        elif thing == 1:
            await ctx.channel.send('304 FTW 🥳🎉')
        elif thing == 2:
            await ctx.channel.send('304 BEST because less stairs')
        elif thing == 3:
            await ctx.channel.send('omg did you know i love 304 wooooo')

    if ctx.content.lower()[0] == 'a':
        thing = random.randint(0, 20)
        if thing == 0:
          await ctx.channel.send('a is for ace-icles')
        elif thing == 1:
          await ctx.channel.send('aaaaaaaaaaaa')

    if ctx.content.lower()[0] == 'hi':
        thing = random.randint(0, 5)
        if thing == 0:
          await ctx.channel.send('greetings!')

    if ctx.content.lower()[0] == 'z':
        thing = random.randint(0, 20)
        if thing == 0:
          await ctx.channel.send('\'m sleepy...💤😪')
        elif thing == 1:
          await ctx.channel.send('i know our curfew\'s at 3.04am but still go sleep pls')

    if 'robot' in ctx.content.lower() or 'bot' in ctx.content.lower():
        thing = random.randint(0, 6)
        if thing == 0:
            await ctx.channel.send('bot! my kin :D')
        elif thing == 1:
            await ctx.channel.send('family? my friends? my life?')
        elif thing == 2:
            await ctx.channel.send('sometimes i can\'t believe i\'m a bot...')
  
    await bot.process_commands(ctx)


keep_alive()
bot.run(TOKEN)
