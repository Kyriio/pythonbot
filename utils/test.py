import requests
#https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner}?api_key=RGAPI-670aede4-e9b3-4776-83fc-26fdeda4a17b
url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Kyriio?api_key=RGAPI-275df423-dd0c-4cec-980f-8713334b8506'
response = requests.get(url)
data = response.json()
print(data)
id_joueur = data['id']

url_rank = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'+id_joueur+'?api_key=RGAPI-275df423-dd0c-4cec-980f-8713334b8506'
response_rank= requests.get(url_rank)

data = response_rank.json()

if (data[0]['queueType']=="RANKED_SOLO_5x5"):
    print("data 0")
    data=data[0]
elif(data[1]['queueType']=="RANKED_SOLO_5x5"):
    print("data 1")
    data=data[1]
else:
    data=data[2]
    print("data 2")

print(data)
print(len(response_rank.json()))

#print(tier) 
#print(tier) 
#print(tier) 2kHI4wa22DdV-7DNMf9KGYmfCouA9ckNcqEjE3kwE54XJkqc


# [{"leagueId":"2dee8c4a-b4a1-4f8b-990c-dae633aeab7b",
#     "queueType":"RANKED_FLEX_SR",
#     "tier":"DIAMOND","rank":"II",
#     "summonerId":"2kHI4wa22DdV-7DNMf9KGYmfCouA9ckNcqEjE3kwE54XJkqc",
#     "summonerName":"1Freazy",
#     "leaguePoints":48,
#     "wins":27,
#     "losses":26,
#     "veteran":false,
#     "inactive":false,
#     "freshBlood":false,
#     "hotStreak":false}
# ,{"leagueId":"9083f362-4a23-3558-b0f1-f2e18476caa8",
#     "queueType":"RANKED_SOLO_5x5",
#     "tier":"GRANDMASTER",
#     "rank":"I",
#     "summonerId":"2kHI4wa22DdV-7DNMf9KGYmfCouA9ckNcqEjE3kwE54XJkqc",
#     "summonerName":"1Freazy",
#     "leaguePoints":664,
#     "wins":224,
#     "losses":187,
#     "veteran":false,
#     "inactive":false,
#     "freshBlood":false,
#     "hotStreak":false}]