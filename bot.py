import discord
import os
from discord.ext import commands
import dotenv
import requests


intents = discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True)
bot = commands.Bot(command_prefix="*",intents=intents)
bot.remove_command('help') # ajout du help perso



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="le serveur"))
    print("Le bot est bien connecté.")


#commande de base ping
@bot.command(name="ping")
async def ping(ctx):
    embed=discord.Embed(description=f'<a:ping_pong:796453534639587377> Pong! {round(bot.latency *1000)}ms', color=0xb0c4de)
    await ctx.send(embed=embed)


#delete des messages
@bot.command(name="del")
@commands.has_permissions(administrator=True)
async def delete(ctx,number_of_messages: int):
    compteur = 0
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for message in messages:
        await message.delete()
        compteur +=1

    embed = discord.Embed(description = f'Nombre de messages supprimés :  {str(compteur-1)}  <a:ok_hand:922894533736411246>', color=0xFF0000)
    await ctx.send(embed=embed)

#Ugg account
@bot.command(name="ugg")
async def ugg(ctx,msg):
    embed = discord.Embed(description=f" <:peposhy:808356222675714058> Ugg de : {msg}  https://u.gg/lol/profile/euw1/{msg}/overview <:peposhy:808356222675714058> ",color =0xFF0000)
    await ctx.send(embed=embed)

#Help
@bot.command(pass_context=True)
async def help(ctx):

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

#donne l'avatar et le pseudo + lvl lol
@bot.command()
async def lol_profile(ctx,name):
    
    url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key='+os.environ['api_lol']
    response = requests.get(url)
    data = response.json()
    name = data['name']
    lvl = data['summonerLevel']
    icon_id= data['profileIconId']

    url_icon = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{icon_id}.png'

    embed=discord.Embed(description=f'Summoner :  **{name}**\n Niveau : **{lvl}**',color=0xFF0000)
    embed.set_image(url=url_icon)
    await ctx.send(embed=embed)


#sert pour la demande d'image sur OPgg
def romain_to_int(num: str) -> int:
    nombre_romain = {
        'I': 1,
        'II': 2,
        'III':3,
        'IV':4,
        'V':5,
    }
    return nombre_romain[num]
#donne le rank de l'utilisateur
@bot.command()
async def rank_lol(ctx,name):
    url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key='+os.environ['api_lol']
    response = requests.get(url)
    data = response.json()

    id_joueur = data['id']
    url_rank = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+id_joueur+'?api_key='+os.environ['api_lol']
    response_rank= requests.get(url_rank)

    data_rank=response_rank.json()

    
    if (data_rank[0]['queueType']=="RANKED_SOLO_5x5"):
        data_rank=data_rank[0]
    elif(data_rank[1]['queueType']=="RANKED_SOLO_5x5"):
        data_rank=data_rank[1]
    else:
        data_rank=data_rank[2]

    tier = data_rank['tier']
    rank = data_rank['rank']
    league_points=data_rank['leaguePoints']
    wins = data_rank['wins']
    losses = data_rank['losses']

    ratio  = wins + losses
    num=romain_to_int(rank)

    url_icon = f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}?image=q_auto:best&v=1'

    embed = discord.Embed(title="Classée solo", description=f' {tier} {rank}',color=0xFF0000)
    embed.set_image(url=url_icon)
    embed.insert_field_at(index=0, name = "LP : ", value = league_points)
    embed.insert_field_at(index=1, name = "Win : ", value = wins)
    embed.insert_field_at(index=2, name = "Losses : ", value = losses)
    embed.insert_field_at(index=3, name = "Winrate : ", value = (round((wins/ratio)*100,2)))

    await ctx.send(embed=embed)

@bot.command()
async def random_meme(ctx):

    url_meme= f'https://meme-api.herokuapp.com/gimme'
    response = requests.get(url_meme)
    data = response.json()
    img = data['url']

    embed = discord.Embed(title="RANDOM MEME", description=f'Je sais pas si il va être drôle mais <a:man_shrugging:923036118931357726>',color=0xFF0000)
    embed.set_image(url=img)

    await ctx.send(embed=embed)


token = os.environ['TOKEN']
bot.run(token)
