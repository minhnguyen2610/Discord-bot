import discord

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

levelOnePower = ["PrincipleAdept", "Iambo"]

#check commands
def checkPermissionLevelOne(ctx):
    return ctx.author.name == levelOnePower[0] 

class Member(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='minh',help='Communist at heart')
    async def minh_2021(self,ctx):
        await ctx.send(f'I am handsome')

    @commands.command(name='peter', help='Kimchi > Sushi')
    async def peter_2021(self, ctx):
        await ctx.send(f'buffalo')

    @commands.command(name='natasha',help='big sis at heart, small sis in brain')
    async def natasha_2021(self, ctx):
        await ctx.send(f'The hobbit')

    @commands.command(name='agustin', help='A simp for Dojo Cat at heart')
    async def agustin_2022(self, ctx):
        await ctx.send(f'Agustin: I aint no simp')

    @commands.command(name='kanita', help='I dont know what to put here')
    async def kanita_2021(self, ctx):
        await ctx.send(f'Short class leader')
    
    @commands.command(name="Victor", help="Welcome to my onlyfan guys")
    async def Victor_2021(self, ctx):
        await ctx.send(f'That is what I have been waiting for, babyyyyyyyyyy')
    
    @commands.command(name="Julia", help="I play League of Legend, and I am good at the game")
    async def Julia_2022(self, ctx):
        await ctx.send(f'hmmmmmmm, funnier than Andy')

    @commands.command(name="Paris", help="The french blunder - classics - Grandmaster Hikaru Nakamori")
    async def Paris_2023(self, ctx):
        await ctx.send(f'Me an intellectual who play League')
    
    @commands.command(name="Andy", help="Dit con me nha may lu cho")
    async def Andy_2021(self, ctx):
        await ctx.send(f'I am the funniest person in this group')
    

def setup(client):
    client.add_cog(Member(client))