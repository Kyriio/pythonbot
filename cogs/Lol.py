import discord
from discord.ext import commands
import requests
import os

def romain_to_int(num: str) -> int:
    nombre_romain = {
        'I': 1,
        'II': 2,
        'III':3,
        'IV':4,
        'V':5,
    }
    return nombre_romain[num]


class Lol(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def ugg(self,ctx,msg):
        embed = discord.Embed(description=f" <:peposhy:808356222675714058> Ugg de : {msg}  https://u.gg/lol/profile/euw1/{msg}/overview <:peposhy:808356222675714058> ",color =0xFF0000)
        await ctx.send(embed=embed)

    #donne l'avatar et le pseudo + lvl lol
    @commands.command()
    async def lol_profile(self,ctx,name):

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

    #donne le rank de l'utilisateur
    @commands.command()
    async def rank_lol(self,ctx,name):
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


    @commands.command()
    async def lastmatch(self,ctx,name):
        url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key='+os.environ['api_lol']
        response = requests.get(url)
        data = response.json()

        puuid= data['puuid']

        print(puuid)

        url_match = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?api_key='+os.environ['api_lol']
        response_match = requests.get(url_match)

        data_match = response_match.json()

        match_1= data_match[0]

        get_info_match = f'https://europe.api.riotgames.com/lol/match/v5/matches/'+match_1+'?api_key='+os.environ['api_lol']
        response_match_infos=requests.get(get_info_match)

        data_end_match = response_match_infos.json()



        for i in range (0,len(data_end_match['info']['participants'])):

            if(data_end_match['info']['participants'][i]['role'] == "NONE"):
                role = ''
            else:
                role = data_end_match['info']['participants'][i]['role']


            embed = discord.Embed(title = f'La dernière game de : {name}'+' Match de type : '+ data_end_match['info']['gameMode']+'',color=0xFF0000)
            embed.set_footer(text=data_end_match['info']['participants'][i]['summonerName'])
            embed.add_field(name='Kills: ', value=data_end_match['info']['participants'][i]['kills'])
            embed.add_field(name='Morts : ', value=data_end_match['info']['participants'][i]['deaths'])
            embed.add_field(name='Assists : ', value=data_end_match['info']['participants'][i]['assists'])
            embed.add_field(name='Role : ', value='**'+data_end_match['info']['participants'][i]['lane']+ ' ' + role +'**')
            embed.set_thumbnail(url='https://ddragon.leagueoflegends.com/cdn/12.1.1/img/champion/'+data_end_match['info']['participants'][i]['championName']+'.png')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Lol(bot))
