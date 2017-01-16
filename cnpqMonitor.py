import datetime
from time import sleep
import urllib.request

url = 'http://www.unisinos.br'
urlNoticia = '/beneficios/mestrado-e-doutorado/cnpq'


print('Como saber se você foi aprovado na bolsa do CNPq?')
print('Fácil, faça um script em Python para verificar')
while 1:
    response = urllib.request.urlopen(url+urlNoticia)
    data  = response.read()
    text = data.decode('utf-8')
    textToFind = 'Confira a lista dos selecionados para bolsa CNPq'
    if textToFind in text:
        text = text[:text.find(textToFind)]
        text = text[text.rfind('href="')+6:]
        text = text[:text.find('"')]
        print(url+text)
        break
    else:
        print('Not Yet.. Last try was: '+ str(datetime.datetime.now()))
    sleep(300)
