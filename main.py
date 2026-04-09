import pandas as pd
import requests
from sqlalchemy import create_engine
from datetime import datetime,timedelta

data_fim = datetime.now().strftime("%d/%m/%Y")
data_inicio = datetime.today() - timedelta(days=365*10)
data_inicio = data_inicio.strftime("%d/%m/%Y")


url_selic = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}")
url_IPCA =  requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}")
url_credito = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20632/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}")#novos empréstimos contratados
url_carteiraCred = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.20540/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}")#Total emprestado até o momento

selic = pd.DataFrame(url_selic.json())
selic['data'] = pd.to_datetime(selic['data'], dayfirst=True)

ipca = pd.DataFrame(url_IPCA.json())
ipca['data'] = pd.to_datetime(ipca['data'], dayfirst=True)

credito = pd.DataFrame(url_credito.json())
credito['data'] = pd.to_datetime(credito['data'], dayfirst=True)

carteiraCred = pd.DataFrame(url_carteiraCred.json())
carteiraCred['data'] = pd.to_datetime(carteiraCred['data'], dayfirst=True)


print(selic.tail())
print(ipca.tail())
print(credito.tail())
print(carteiraCred.tail())
