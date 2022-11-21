import json
import requests
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
moeda = json.loads(requisicao.text)['USDBRL']['high']
print("1 Dolar custa: "+ moeda +" Reais")

#Uso de API aula 13
