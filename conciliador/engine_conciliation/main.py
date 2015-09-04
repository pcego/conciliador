import urllib3, json

http = urllib3.PoolManager()
r = http.request('GET', 'http://worldcup.sfg.io/matches')

for jogo in json.loads(r.data.decode('utf-8')):
    if jogo['status'] == 'completed':
        print (jogo['home_team']['country'], jogo['home_team']['goals'], 'x', jogo['away_team']['country'], jogo['away_team']['goals'])