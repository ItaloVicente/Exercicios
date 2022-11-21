import requests
import json
cep = input("Digite seu CEP (somente 8 numeros): ")
requisicao = requests.get("http://viacep.com.br/ws/"+cep+"/json/")
json = json.loads(requisicao.text)
print()
print("=========================================")
print("Consulta de CEP")
print()
for i in json:
    print(i.title()+": "+ json[i])
print("=========================================")
#60751230