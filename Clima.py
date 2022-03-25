import requests
from bs4 import BeautifulSoup

siteclima = 'https://www.cptec.inpe.br/'
pagina = requests.get(siteclima)
soup = BeautifulSoup(pagina.text, 'html.parser')

clima = str(soup.find_all(class_='bloco-previsao d-flex flex-column text-center'))

print(f'~ Temp. Máxíma: {clima[112:115]} Graus Celsius\n'
      f'~ Temp. Minima: {clima[175:178]} Graus Celsius\n'
      f'~ Humidade: {clima[312:314]} \n')










"""for listagem in data:
    if cidade in listagem:
        print(bool(listagem))"""   #MOSTRAR A CIDADE[TRUE OU FALSE]


