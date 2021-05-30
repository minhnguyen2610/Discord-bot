import discord

import random

from discord.ext import commands

listOfMember = {
    "Tashee":702740671186075659,
    "BOSS BABY":488061960974237696,
    #bot owner
    "ThousandFaces":578333246618599458,
    "Kanita":812189623315857430,
    #admin
    "Iambo":567788833266204672,
    "Silver":624727790209466382,
    "Jujubinha":368392468548419584
}

levelOnePower = ["PrincipleAdept","GOD BABY", "Silver", "Kanita", "Iambo", "Null","PoPotato9742", "Jujubinha"]

#check commands
def checkPermissionLevelOne(ctx):
    if ctx.author.name == levelOnePower[0] or ctx.author.name == levelOnePower[1] or ctx.author.name == levelOnePower[2] or ctx.author.name == levelOnePower[3] or ctx.author.name == levelOnePower[4] or ctx.author.name == levelOnePower[5] or ctx.author.name == levelOnePower[6] or ctx.author.name == levelOnePower[7]:
        return True


trashTalkContainer = {
    "encouragement": [
        "GG guys",
        "Amazing plays",
        "You completely crush the enemy team",
        "I am seeing future challengers in this team",
        "Oh dear, oh dear, gorgeous"
    ],
    "trashTalk": [
        "You fucking donkey",
        "Did your mom drop you on the head when you were young?",
        "You noob, go back to bronze rank",
        "Wow, I never know that someone of your skill can be this bad",
        "Your mom"
    ],
}


def checker(word):
    word = word.lower()
    if "win" in word or "yay" in word or "we win" in word or "we won" in word or "hell ya" in word:
        return True
    elif "lost" in word or "lose" in word or "fuck" in word:
        return False
    else:
        return False

class League(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is COG-ready")

    @commands.command(name="leagueTalk", help="Encouragement for LOL players")
    async def leagueTalk(self, ctx, *, stateOfGame):
        if checker(stateOfGame):
            await ctx.send(random.choice(trashTalkContainer["encouragement"]))
        else:
            await ctx.send(random.choice(trashTalkContainer["trashTalk"]))

    @commands.command(name="troll", help="To spam - use .troll[space][number of spam you want][space][message to spam]")
    @commands.check(checkPermissionLevelOne)
    async def troll(self, ctx, numberOfTroll, *,contentToSpam):
        numberOfTroll = int(numberOfTroll)
        if contentToSpam == "peter":
            for x in range(numberOfTroll):
                await ctx.send("이상인")
        else:
            for x in range(numberOfTroll):
                await ctx.send(contentToSpam)
    
#command to load the cog up into client. NEED. MUST HAVE
def setup(client):
    client.add_cog(League(client))