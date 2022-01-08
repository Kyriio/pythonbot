import discord
from discord.ext import commands
import os


class admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def whois(self,ctx,member : discord.Member=None):
        if not member:
            member = ctx.message.author
            
        roles = [role for role in member.roles]
        embed = discord.Embed(color=0xFF0000, timestamp=ctx.message.created_at,title=f'Infos - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Demandé par {ctx.author}')
        embed.add_field(name='ID: ' , value = member.id,inline=False)
        embed.add_field(name='Nom : ', value=member.display_name,inline=False)
        embed.add_field(name='Compte créé : ', value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
        embed.add_field(name='A rejoint le : ', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        embed.add_field(name='Roles : ', value=' '.join([role.mention for role in roles]),inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(admin(bot))
