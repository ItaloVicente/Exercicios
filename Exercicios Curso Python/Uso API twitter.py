import oauth2
import json
import urllib.parse

#Para rodar esse programa precisa de mais acesso, o Twitter limitou as permissoes de requisicao
consumer_key = 'netMU2SHXBLUOwSJNZW3ydA9x'
consumer_secret = 'tihISVjAnLSCTMIhsfZNATzrT9HQBEGdE6rJKmCXiAXJy4lqNx'

token_key = '1334815378095169536-D3vp4F2USLjqEyYUBSXtjS8FttNAUS'
token_secret = 'IQNyB3HDyiV4w4r2CVl0H5b7YgFSBhGy29Y8X7XPX6UVo'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
print(objeto)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()

