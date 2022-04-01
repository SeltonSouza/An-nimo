import pandas as pd
from twilio.rest import Client

#se for rodar esse projeto não se esqueça de intala a bribiotéca openpyxl com o comando (pip install openpyxl).
#para a pandas conseguir ler os arquivos xlsx.


# Your Account SID from twilio.com/console
 #esse é o meu account_sid, você tem que criar uma conta no twilio
account_sid = "ACc50e8b2505377341c83c9f4ca0a5eb0c"
# Your Auth Token from twilio.com/console
#esse é o meu auth_token crie o seu no twilio
auth_token  = "8d48edc16e1752ee52e480e716a776a5" 
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#for para abrir cada aquivo Ecxel dinamicamente 
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas ['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc [tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc [tabela_vendas ['Vendas'] > 55000, 'Vendas'].values[0]
        #mensagem enviada se a condição for satisfeita
        message = client.messages.create(
            to="+5521995277386", 
            from_="+19124546941",
            body=f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
