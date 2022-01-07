import discord
import os
from discord import client
from discord.ext import commands
import dotenv
import requests
from config import api_lol, TOKEN


class base(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #commande de base
    
    @commands.command()
    async def ping(self,ctx):
        embed=discord.Embed(description=f'<a:ping_pong:796453534639587377> Pong! {round(self.bot.latency *1000)}ms', color=0xb0c4de)
        await ctx.send(embed=embed)


    #delete des messages
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self,ctx,number_of_messages: int):
        compteur = 0
        messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

        for message in messages:
            await message.delete()
            compteur +=1

        embed = discord.Embed(description = f'Nombre de messages supprimés :  {str(compteur-1)}  <a:ok_hand:922894533736411246>', color=0xFF0000)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def help(self,ctx):

        embed=discord.Embed(title='Liste des commandes',color=0xFF0000)
        embed.add_field(name=' ⁢', value='-help:  **(Montre les commandes.)**',inline=False)
        embed.add_field(name=' ⁢', value="-ping **(Donne la latence entre vous et le bot)**",inline=False)
        embed.add_field(name=' ⁢', value="-lol_profile nom **(Donne l'icone et le lvl d'un invocateur)**",inline=False)
        embed.add_field(name=' ⁢', value="-rank_lol nom **(Donne le rank de l'invocateur)**",inline=False)
        embed.add_field(name=' ⁢', value="-ugg nom **(Donne le lien ugg d'un invocateur)**",inline=False)
        embed.add_field(name=' ⁢', value="-random_meme **Tout est dans le nom**",inline=False)
        embed.add_field(name=' ⁢', value="-del x **(Supprime le nombre de messages (modo uniquement))**",inline=False)
        embed.set_footer(text='[Prefix: * ]')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(base(bot))
