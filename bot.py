import os
import discord

import random

from dotenv import load_dotenv
from discord.ext import commands

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
        await ctx.send('hi tongyu')

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

    if 'hate' in ctx.content.lower() and ('haiku bot' in ctx.content.lower() or 'haikubot' in ctx.content.lower()):
        thing = random.randint(0, 2)
        if thing == 0:
            await ctx.channel.send('i hate haiku bot too')
        if thing == 1:
            await ctx.channel.send("you're so mean to haiku baby😤")
        if thing == 2:
            await ctx.channel.send('haiku bot <3')

    if '304' in ctx.content.lower():
        thing = random.randint(0, 4)
        if thing == 0:
            await ctx.channel.send('i LOVE 304!!! <333')
        elif thing == 1:
            await ctx.channel.send('304 FTW 🥳🎉')


    await bot.process_commands(ctx)




bot.run(TOKEN)
