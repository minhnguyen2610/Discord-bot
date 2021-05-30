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

levelOnePower = ["ThousandFaces", "PrincipleAdept", "Iambo","Tashee"]

#check commands
def checkPermissionLevelOne(ctx):
    return ctx.author.name == levelOnePower[0] or ctx.author.name == levelOnePower[1] or ctx.author.name == levelOnePower[2]

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is COG-ready")

    #command
    @commands.command(help='Kick people from the server with the format of .kick[space][name][space][reason]')
    @commands.check(checkPermissionLevelOne)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'lol, bye {member.mention}')

    @commands.command(help='Ban people from the server with the format of .ban[space][name][space][reason]')
    @commands.check(checkPermissionLevelOne)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'banned {member.mention}')

    @commands.command(help='Unban people from the server with the format of .unban[space][name + id number]')
    @commands.check(checkPermissionLevelOne)
    async def unban(self, ctx,*,member): 
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entries in banned_users: 
            user = ban_entries.user
            if (user.name, user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unban {user.name}#{user.discriminator}')
                return

    @commands.command(help='Clear text, duh.')
    async def clear(self, ctx, amount = 3):
        await ctx.channel.purge(limit = amount)
        await ctx.send("Deleted")

#command to load the cog up into client. NEED. MUST HAVE
def setup(client):
    client.add_cog(Admin(client))