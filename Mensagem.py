import csv
import datetime
import pytz
import pywhatkit as pw
from icecream import ic

# Carregue os dados a partir do arquivo CSV
with open('Contatos.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    contatos = [row for row in reader]

# Configure o fuso horário local
timezone = pytz.timezone('America/Sao_Paulo')

#Pegando o dia atual
data_atual = datetime.date.today()
dia = data_atual.day

celulares = []

for contato in contatos:
    # Converte o valor da coluna 'Numero' para um inteiro
    diaPag = int(contato['Numero'])

    # Verifica se o número é dias antes do dia atual
    if dia + 1 == diaPag :
        nome = contato['Nome']
        numCel = contato['Codigo']
        if numCel != ' 0000':
            celulares.append(numCel)


pw.open_web()

for numero in celulares:
    pw.sendwhatmsg_instantly(f"+55 {numero}","Ola")
    

