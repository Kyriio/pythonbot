import requests

class LolSettings:
    def __init__(self,summoner,region):
        self.summoner = summoner
        self.region= region
            
        
    def start(self):
        url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner}?api_key=RGAPI-670aede4-e9b3-4776-83fc-26fdeda4a17b'
        response = requests.get(url)
        return response.json()

class Lol(LolSettings): #definir la fonction
    def __init__(self,summoner,region):
        super().__init__(summoner,region)

    def greetings(self):
        summoner = self.start()
        name = summoner['name']
        lvl = summoner['summonerLevel']
        icon_id = summoner['profileIconId']

        greetings = f'Bonjour invocateur {name}, lvl {lvl}.'
        icon_url = f'https://ddragon.leagueoflegends.com/cdn/11.24.1/img/profileicon/{icon_id}.png'
        return {'greetings': greetings, 'icon_url': icon_url}