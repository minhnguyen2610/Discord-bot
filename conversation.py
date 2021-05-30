import discord
import random
import math
import time

from discord.ext import commands

#detail about member of chat
listOfMember = {
    "Tashee":702740671186075659,
    "BOSS BABY":488061960974237696,
    #bot owner
    "ThousandFaces":578333246618599458,
    "Kanita":812189623315857430,
    #admin
    "Iambo":567788833266204672
}

levelOnePower = ["ThousandFaces", "Iambo"]

class conver(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="Introduction", help='Introduce yourself Goat')
    async def intro(self,ctx):
        await ctx.send("Bow down to your king you mongrols")

    @commands.command(name='mathGod', help='Test your math skill')
    async def mathGod(self, ctx):
        firstTerm = random.randint(1,1000)
        secondTerm = random.randint(1,1000)
        answer = firstTerm + secondTerm
        await ctx.send(f'What is {firstTerm} + {secondTerm}?')
        time.sleep(3)
        await ctx.send(f'It is {answer}')

    @commands.command(name="success", help="Boost the programmer's ego")
    async def success(self, ctx):
        await ctx.send(f'{ctx.author} is a god')

    # *, question allow multiple parameters to be taken in as one parameter
    @commands.command(name='_8ball', help='Let the robot truthfully answer some of your question.')
    async def _8ball(self, ctx, *, question):
        answer = [
            'It is certain',
            'Without a doubt',
            'You may rely on it',
            'Yes definitely',
            'It is decidedly so',
            'As I see it, yes',
            'Most likely',
            'Yes',
            'Outlook good',
            'Signs point to yes',
            'You are ugly.',
            "No, no, and no",
            'Never gonna give you up, never gonna let you down, never gonna run around and hurt you',
            "Decisively negative",
            "I don't want to roast you because my mom said that I shouldn't burn trash",
            "your mom",
            "Hell no",
            "Tu es muy stupito",
            "When pigs know how to flies",
            "Bruh u fat",
            "I am smart",
            "You know the rule and so do I"
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(answer)}')
        


def setup(client):
    client.add_cog(conver(client))