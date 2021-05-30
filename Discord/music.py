import random
import math
import time
import os
import discord
import youtube_dl
import shutil
import asyncio

from discord.ext import commands, tasks

#queue. Store music. After song ended, play next song. Delete current song. 

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []

    @commands.command(help="Play music by using an url")
    async def play(self, ctx, *, url : str):

        # channel = ctx.author.voice.channel
        song_there = os.path.isfile("song.mp3")
        voice_connected = ctx.voice_client
        voice_channel = ctx.author.voice.channel.name
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        self.queue.append(url)

        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            # await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            # return
            await ctx.send(f'{url} added to queue')
            return

        if not voice_connected:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name= voice_channel)
            await voiceChannel.connect()

        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'default_search': 'ytsearch', #best shet ever
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        } 
        #this whole function is new
        def playNextSong():
            del self.queue[0]
            if len(self.queue) > 0:
                if song_there:
                    os.remove("song.mp3")
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    #downloading song for self.queue from youtube
                    ydl.download([self.queue[0]])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: playNextSong())
            else:
                return

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #meta here is a giga dictionary contain a bunch of info of self.queue[0]
            meta = ydl.extract_info(self.queue[0])
            entry = meta["entries"][0]["title"]
            #downloading song for self.queue from youtube
            ydl.download([self.queue[0]])
            await ctx.send(f'Now playing {entry}')
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: playNextSong())
            

    @commands.command(help="basically kicking the bot out of the voice channel")
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")
    
    @commands.command(name='queue', help='Command .queue show to show queue')
    async def _queue(self,ctx):
        #if statement here was new. Before: await ctx.send(self.queue)
        if len(self.queue) > 0:
            for i in range(len(self.queue)):
                await ctx.send(f"{i+1}. {self.queue[i]}")
        else:
            await ctx.send("Currently, there is no song in queue")


    @commands.command(help='Pause music')
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("What are you stopping?")


    @commands.command(help='Resume paused music, not stopped music')
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Don't ask for a universal pause continue button")


    @commands.command(name="stop", help ="stop the music, for good.")
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()

    # @commands.command(name="queue", help="queue for music")
    # async def _queue(self, ctx, url:str):



def setup(client):
    client.add_cog(Music(client))