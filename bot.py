import os
import discord

from random import *
import pickle

from dotenv import load_dotenv
from discord.ext import commands
from mcstatus import MinecraftServer
from datetime import *

from keep_alive import keep_alive

from small import nya, oo

from dnd import *

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='~')
bot.remove_command("help")

error = ("sorry, couldn't understand")

server = MinecraftServer.lookup("curfew_at_404.aternos.me:44614")


dnd_players = {}


def save_obj(obj, name):
    try:
        os.makedirs('saves')
    except:
        pass

    with open('saves/'+ name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('saves/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


@bot.event
async def on_ready():
    global dnd_players

    await bot.change_presence(activity=discord.Game('with 404\'22! | ~help'))
    #try:
    dnd_players = load_obj('dnd_players')
    for key, value in dnd_players.items():
        try:
            if value.money:
                pass
        except:
            dnd_players[key] = Player(dnd_players[key].user, dnd_players[key].abilities, dnd_players[key].name)

        finally:
            print(vars(dnd_players[key]))

    #except:
    #    dnd_players = {}

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
> `~help` to show this page!
> `~ping` to test if the bot is online
> `~alphabet` to show the gay alphabet
> `~github` to find the link to the bot's github repo
> `~minecraft` to get the status of the minecraft server!
> `~nya [text]` and `~oo [text]` are some pretty fun commands too :)
> `~pride` tells you how far away pride month is :D
> `~dnd` is a sub-module that contains a very stripped-down dnd bot. try `~dnd help` to see what it has!
> `~gpa find` can help you calculate how much you have to score to reach a certain gpa! yay.

> i also sometime respond to messages ^^
    """)


@bot.command("alphabet")
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

@bot.command('github')
async def github(ctx):
    e = discord.Embed(title="304bot's github",
                      url="https://github.com/fqdingsky/304bot",
                      description="github repository for 304bot's code!")
    await ctx.send(embed=e)

@bot.command('test')
async def test(ctx):
    if ctx.author.id == 670962000964354049:
        await ctx.send("tongyu testing :D")

@bot.command('minecraft')
async def minecraft(ctx):

    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    try:
      status = server.status()

      list = []

      for person in status.players.sample:
          #print(person.name)
          list.append(person.name)

      #print("some people are online! they are: {0}".format(", ".join(list)))

      await ctx.send("some people are online at curfew_at_404.aternos.me! they are: {0}".format(", ".join(list)))
    except:
      await ctx.send("server is offline. turn it on! :D")

@bot.command('nya')
async def nya_(ctx, *args):
    await ctx.send(nya(" ".join(args[:])))

@bot.command('oo')
async def oo_(ctx, *args):
    await ctx.send(oo(" ".join(args[:])))

@bot.command('pride')
async def pride(ctx):
    response = ""
    if date.today().month == 6:
        response += "we're in pride month!! :rainbow_flag: :tada: :partying_face:"
    else:
        if date.today().month < 6:
            pridemonth = date(date.today().year, 6, 1)
        else:
            pridemonth = date(date.today().year + 1, 6, 1)
        response += str((pridemonth - date.today()).days) + " days left to pride month!"

    await ctx.send(response)

@bot.command("gpa")
async def gpa(ctx, way = "query"):
    gpas = {
    "4.0": 80,
    "3.6": 70,
    "3.2": 65,
    "2.8": 6,
    "2.4": 55,
    "2.0": 50,
    "1.6": 45,
    "1.2": 40
    }
    find_alias = ["howmuch", "find"]
    query_alias = ["calculate", "query"]

    def check(message):
        return message.author.id == ctx.message.author.id and message.content != ""


    if way in find_alias:
        gpa = 0
        aim = ""
        while gpa == 0:
            await ctx.send("ok, i'll help you find how much you need to score in order to reach a certain gpa. what's your target gpa?")
            message = await bot.wait_for(
                "message", timeout=120, check=check
            )
            if message.content.lower() in gpas.keys():
                gpa = gpas[message.content.lower()]
                aim = message.content.lower()
                await ctx.send("great! please send your current grades in the format `[marks] [fullscore] [percentage]`, such as `20 25 10`. type quit anytime to abort, and type done to finish.")
                message = await bot.wait_for(
                    "message", timeout=120, check=check
                )

        count = 0.0
        weightages = 0
        fullscore = 0

        while message.content.lower() not in ["done", "quit", "exit"]:
            values = message.content.lower().split(" ")
            try:
                count += (float(values[0]) / float(values[1])) * float(values[2])
                weightages += int(values[2])
            except:
                await ctx.send("couldn't read that D:")

            message = await bot.wait_for(
                "message", timeout=120, check=check
            )

        if message.content.lower() == "done":
            await ctx.send("nice! okay. what's the full score for your final paper?")
            while fullscore == 0:
                message = await bot.wait_for(
                    "message", timeout=120, check=check
                )
                try:
                    fullscore = int(message.content.lower())
                except:
                    await ctx.send("i couldn't read that >:(")

            score_needed = (gpa - count) / (100 - weightages) * fullscore
            await ctx.send("you need a score of " + str(score_needed) + "/" + str(fullscore) + " to score a gpa of " + aim)


        elif message.content.lower() in ["quit", "exit"]:
            await ctx.send("aborting :)")




    elif way == "help":
        await ctx.send("sorry there's no documentation. ask someone who knows or search the chat lol.")

    elif way in query_alias:
        pass
        #calculate cur gpa

    else:
        await ctx.send("sorry idk what you're saying :(")




@bot.command('dnd', aliases = ['d&d', 'd'])
async def dnd(ctx, do = "help", what = "", additional = 0, person: discord.User = None, *args):
    global dnd_players

    def check(message):
        return message.author.id == ctx.message.author.id and message.content != ""

    try:
        if not additional.lstrip("-").isdigit() or not isinstance(additional, (int, float)):
            who = additional
    except:
        pass

    if person == None:
        who = ctx.author
    else:
        who = person



    if do == "player":
        if what == "create":
            dnd_players[who.id] = Player(who)
            sent_initial_message = await ctx.send(
            "creating dnd character for you... follow the instructions!\n\nyour character has 6 abilities: strength, dexterity, constitution, intelligence, wisdom, and charisma.\nthese abilities can have a score of 15, 14, 13, 12, 10, or 8."
            )
            abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
            scores = [15, 14, 13, 12, 10, 8]

            await ctx.send("but first, what's your character's name?")
            message = await bot.wait_for(
                "message", timeout=120, check=check
            )
            dnd_players[who.id].set_name(message.content.lower())

            await ctx.send("that's a good name.")
            for i in range(6):
                await ctx.send("\n\nwhich ability would you like to use the score of " + str(scores[i]) + " on?")
                done = False
                while done == False:
                    message = await bot.wait_for(
                        "message", timeout=120, check=check
                    )

                    if message.content.lower() in abilities:
                        dnd_players[ctx.author.id].update_ability(message.content.lower(), scores[i])
                        await ctx.send("set " + message.content.lower() + " to " + str(scores[i]) + ".")
                        abilities.remove(message.content.lower())
                        done = True

                    elif message.content.lower() in ["cancel", "quit", "exit"]:
                        dnd_players.pop(ctx.author.id, None)
                        await ctx.send("character creation cancelled. see you!")
                        return

                    else:
                        await ctx.send("that's not a valid option!")

            text = "your character, " + dnd_players[who.id].name + ", is created with the following abilities:\n"
            for i in range(6):
                ability = list(dnd_players[who.id].abilities.keys())[i]
                text += ability + " - " + str(dnd_players[who.id].abilities[ability]) + "\n"

            await ctx.send(text)
            save_obj(dnd_players, "dnd_players")

        elif what in ["query", "info"]:
            #print(vars(dnd_players[who.id]))

            text = "your character, " + dnd_players[who.id].name + ", has the following abilities:\n"
            for i in range(6):
                ability = list(dnd_players[who.id].abilities.keys())[i]
                text += ability + " - " + str(dnd_players[who.id].abilities[ability]) + " (modifier: " + str(floor((dnd_players[who.id].abilities[ability] - 10) / 2)) + ")\n"
            text += "you also have " + str(dnd_players[who.id].money) + " coins."
            await ctx.send(text)

        elif what in ["money", "coins", "coin"]:
            dnd_players[who.id].add_money(additional)
            await ctx.send("you added " + str(additional) + " coins to " + dnd_players[who.id].name + ". they have " + str(dnd_players[who.id].money) + " coins now.")

        elif what in ["item", "thing", "take"]:
            await ctx.send("what does " + dnd_players[who.id].name + " pick up?")
            message = await bot.wait_for(
                        "message", timeout=120, check=check
                    )
            dnd_players[who.id].add_item(message.content.lower())
            await ctx.send(dnd_players[who.id].name + " picks up the " + message.content.lower() + ".")

        elif what in ["drop", "throw", "destroy", "use", "lose"]:
            await ctx.send("what does " + dnd_players[who.id].name + " drop?")
            message = await bot.wait_for(
                        "message", timeout=120, check=check
                    )
            if message.content.lower() in dnd_players[who.id].items:
                dnd_players[who.id].remove_item(message.content.lower())
                await ctx.send(dnd_players[who.id].name + " loses the " + message.content.lower() + ".")
            else:
                await ctx.send("you don't have that!")

        elif what in ['i', 'inventory', 'items', 'inv']:
            await ctx.send("you have: " + ', '.join(dnd_players[who.id].items) + '.')


    elif do == "roll":

        if what in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            await ctx.send(dnd_players[who.id].roll(what, int(additional)))

        else:
            try:
                if 'd' in what:
                    dice_count = int(what.split('d')[0])
                    if dice_count == '':
                        dice_count = 1
                    dice_num = int(what.split('d')[1])
                else:
                    dice_count = 1
                    dice_num = int(what)
                result = roll(dice_count, dice_num, additional)

                reply = "you rolled a "
                first = True
                for i in result[0]:
                    if not first:
                        reply += ", "
                    else:
                        first = False
                    reply += str(i)

                reply += "."


                if additional != 0:
                    reply += "\nyou also added a modifier of " + str(additional) + '.'

                if dice_count > 1 or additional != 0:
                    reply += "\nthat puts your total at " + str(result[1]) + '.'
                await ctx.send(reply)
            except:
                await ctx.send("that's not a valid roll!")

    elif do == "help":
        await ctx.send("""
        > welcome to the dnd module!
        > the dnd parts of me can only keep track of player abilities and roll dice. but i think it's quite a lot :)
        > aliases: `~dnd`, `~d`, `~d&d`

        > current commands:
        > `~dnd help` to show this page!
        > `~dnd player` includes `~dnd player create`, which brings you through an interactive menu to create your dnd character, as well as `~dnd player query`, which tells you the stats of your character.
        > `~dnd roll [ability] [advantage]` rolls a die. without the extra bits, it rolls a 1d20. you can add an ability to calculate the value based on your ability modifiers, as well as `1` or `-1` under advantage to get an advantage or disadvantage.

        > that's about it for now! more will be added maybe :D
            """)


    else:
        await ctx.send("sorry that's not a thing (yet) D:")


@bot.event
async def on_member_join(member):
    await bot.get_channel(788726154269294635).send("welcome to 304's class discord server, " + member.mention + "! i'm your local 304 class bot :D hope you enjoy your time here! do send an intro in " + bot.get_channel(788772685131415602).mention + ".")

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user or ctx.channel.id == 879153478935654420:
        return

    message = ctx.content.lower().split()

    if 'happy birthday' in ctx.content.lower():
        await ctx.channel.send('happy birthday!🎈🎉')

    # if 'aro' in message:
    #     thing = randint(0, 15)
    #     if thing == 0:
    #         await ctx.channel.send('aromatic 🕯')
    #     elif thing == 1:
    #         await ctx.channel.send('aerodynamic aros')
    #     elif thing == 2:
    #         await ctx.channel.send('why ship when you can aro-plane people?')
    #     elif thing == 3:
    #         await ctx.channel.send('two aros sitting in a tree \n s-i-t-t-i-n-g')
    #     elif thing == 4:
    #         await ctx.channel.send('🏹 a r r o w')
    #     elif thing == 5:
    #         await ctx.channel.send('aro rights!')
    #
    # if 'gay' in message:
    #     thing = randint(0, 15)
    #     if thing == 0:
    #         await ctx.channel.send('GAYYYYYYYYY')
    #     elif thing == 1:
    #         await ctx.channel.send('gay rights babey!')
    #     elif thing == 2:
    #         await ctx.channel.send('let\'s go gaymers')
    #     elif thing == 3:
    #         await ctx.channel.send('🥳🎉🏳️‍🌈')
    #     elif thing == 4:
    #         await ctx.channel.send('e is for elmo')
    #     elif thing == 5:
    #         await ctx.channel.send('hi this is 304 bot um sorry for disturbing but i think i\'m, uh, coming out as gay! yee')
    #     elif thing == 6:
    #         await ctx.channel.send('i am a secret gaygent and i\'m spying shh')
    #
    # if 'ace' in message:
    #     thing = randint(0, 15)
    #     if thing == 0:
    #         await ctx.channel.send('i aced my bot exams to become a real bot :D')
    #     elif thing == 1:
    #         await ctx.channel.send("welcome to ace hardware there's no screwing just tons of screws")
    #     elif thing == 2:
    #         await ctx.channel.send('ACE-OLOTL!!')
    #     elif thing == 3:
    #         await ctx.channel.send('||wait... if i\'m ace and you\'re ace who gives a fuck?||')
    #     elif thing == 4:
    #         await ctx.channel.send('instead of coming out of the closet i came out of the deck!! :D')
    #     elif thing == 5:
    #         await ctx.channel.send("please don't hug asexuals you gotta embr**ace** them")
    #
    # if 'bi' in message:
    #     thing = randint(0, 15)
    #     if thing == 0:
    #         await ctx.channel.send('bisexuals are werewolves confirmed')
    #     elif thing == 1:
    #         await ctx.channel.send("a bisexual witch call that a bihexual")
    #     elif thing == 2:
    #         await ctx.channel.send('ways to attract a bisexual: make lots of bi puns')
    #     elif thing == 3:
    #         await ctx.channel.send('bi-derman bi-derman')
    #     elif thing == 4:
    #         await ctx.channel.send('hey all my bi babies out there please check your posture')
    #     elif thing == 5:
    #         await ctx.channel.send("pray for all the bisexual's ankles during this cold time😔")
    #
    # if 'haiku bot' in message or 'haikubot' in message or 'haiku' in message:
    #     thing = randint(0, 5)
    #     if thing == 0:
    #         await ctx.channel.send('... did someone mention haikubot?')
    #     if thing == 1:
    #         await ctx.channel.send("you're so mean to haiku baby😤")
    #     if thing == 2:
    #         await ctx.channel.send('haiku bot :O')
    #     if thing == 3:
    #         await ctx.channel.send('i hate haikubot too')


    if 'scream with me gaybie' in ctx.content.lower():
      await ctx.channel.send('aaaaaaaaaaa')

    elif 'gaybie kill them' in ctx.content.lower():
      await ctx.channel.send('THEY HAVE BEEN STAB\'D! CRIMES :dagger:')

    # elif '304 bot' in message or 'gaybie' in message:
    #     thing = randint(0, 10)
    #     if thing == 0:
    #         await ctx.channel.send('did someone call me?')
    #     elif thing == 1:
    #         await ctx.channel.send('is anyone talking about me behind my back 👀')
    #     elif thing == 2:
    #         await ctx.channel.send('love me take me kiss me get me closer!')
    #     elif thing == 3:
    #         await ctx.channel.send('you called?')
    #     elif thing == 4:
    #         await ctx.channel.send('i\'m a gay baby i\'m a gaybie')
    #
    #
    # elif '304' in message:
    #     thing = randint(0, 10)
    #     if thing == 0:
    #         await ctx.channel.send('i LOVE 304!!! <333')
    #     elif thing == 1:
    #         await ctx.channel.send('304 FTW 🥳🎉')
    #     elif thing == 2:
    #         await ctx.channel.send('304 BEST because less stairs')
    #     elif thing == 3:
    #         await ctx.channel.send('omg did you know i love 304 wooooo')
    #
    # if 'should up' in ctx.content.lower():
    #   await ctx.channel.send('should up? \*zips mouth*')
    #
    #
    # if message[0][0] == 'a':
    #     thing = randint(0, 20)
    #     if thing == 0:
    #       await ctx.channel.send('a is for ace-icles')
    #     elif thing == 1:
    #       await ctx.channel.send('aaaaaaaaaaaa')
    #
    # if 'hi' in message:
    #     thing = randint(0, 5)
    #     if thing == 0:
    #       await ctx.channel.send('greetings!')
    #
    # if message[0][0] == 'z':
    #     thing = randint(0, 20)
    #     if thing == 0:
    #       await ctx.channel.send('\'m sleepy...💤😪')
    #     elif thing == 1:
    #       await ctx.channel.send('i know our curfew\'s at 3.04am but still go sleep pls')
    #
    # if 'robot' in message or 'bot' in message:
    #     thing = randint(0, 15)
    #     if thing == 0:
    #         await ctx.channel.send('bot! my kin :D')
    #     elif thing == 1:
    #         await ctx.channel.send('family? my friends? my life?')
    #     elif thing == 2:
    #         await ctx.channel.send('sometimes i can\'t believe i\'m a bot...')

    if 'flavouring' in message or 'flavoring' in message:
      thing = randint(0, 3)
      if thing == 0:
        await ctx.channel.send('NOT TASTY. WOULD NOT RECOMMEND.')
      elif thing == 1:
        await ctx.channel.send('maggie mee')

    await bot.process_commands(ctx)

keep_alive()
bot.run(TOKEN)
