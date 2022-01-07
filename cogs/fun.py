import discord
from discord.ext import commands
import requests
import os

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @commands.command()
    async def avatar(self,ctx,member : discord.Member = None):
        if member is None:
            embed = discord.Embed(title=f"L'Avatar de : {ctx.author}", color =0xFF0000)
            embed.set_image(url=ctx.author.avatar_url)
        else:
            embed = discord.Embed(title=f"L'Avatar de : {member} ",color=0xFF0000)
            embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def random_meme(self,ctx):

        url_meme= f'https://meme-api.herokuapp.com/gimme'
        response = requests.get(url_meme)
        data = response.json()
        img = data['url']

        embed = discord.Embed(title="RANDOM MEME", description=f'Je sais pas si il va être drôle mais <a:man_shrugging:923036118931357726>',color=0xFF0000)
        embed.set_image(url=img)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
