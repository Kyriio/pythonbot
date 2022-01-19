from calendar import c
import discord
import os
from discord import client
from discord.ext import commands
from datetime import datetime



class Logs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message_delete(self,message):
        channel = self.bot.get_channel(int(933460454515302430))

        message_createeed=message.created_at.strftime('%Y-%m-%d %H:%M:%S %Z%z')

        embed = discord.Embed(title=f'Message supprimé de : {message.author} \n Le  : {message_createeed}',color = 0xFF0000)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name='Message :  ', value = message.content)



        await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        channel = self.bot.get_channel(int(933460454515302430))

        modified=datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        embed = discord.Embed(title=f'Message modifié de : {before.author} \n Le  : {modified}',color = 0xFF0000)

        embed.set_thumbnail(url=before.author.avatar_url)
        embed.add_field(name ='Message avant édition :', value = before.content,inline=False)
        embed.add_field(name=' Message après édition :' , value = after.content,inline=False)

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self,before,after):
        channel = self.bot.get_channel(int(933460454515302430))
        modified=datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        roles = [role for role in after.roles]

        roles_before = [role for role in before.roles]

        if len(before.roles) != len(after.roles):

            embed = discord.Embed(title =f'Les rôles ont été changé pour : {after} \n Le : {modified}',color = 0xFF0000)
            embed.set_thumbnail(url=before.avatar_url)
            embed.add_field(name='Liste des nouveaux rôles : ', value=' '.join([role.mention for role in roles]),inline=False)
            embed.add_field(name='Liste des anciens rôles : ', value=''.join([role.mention for role in roles_before]),inline=False)


            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Logs(bot))
