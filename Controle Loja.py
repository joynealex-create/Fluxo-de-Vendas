#Passo1 = Percorrer todos os arquivos da pasta base de dados (Pasta Vendas).

import os
import pandas as pd
import matplotlib.pyplot as plt

lista_arquivos = os.listdir('/content/drive/MyDrive/Vendas')
tabela_total = pd.DataFrame()


#Passo2 = Importar base de dados de Vendas.
for arquivo in lista_arquivos:
  if "Vendas" in arquivo:

     tabela = pd.read_csv(f"/content/drive/MyDrive/Vendas/{arquivo}")
     # Concatenar DataFrames usando pd.concat() em vez de .append()
     tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

# Exibir a tabela total após o loop
#display(tabela_total)

#Passo3 = Tratar/compilar base de dados de vendas.

#Passo4 = Calcular produto mais vendido (quantidade).
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida','Preco Unitario']].sort_values(by='Quantidade Vendida', ascending=False)
display(tabela_produtos)

#Passo5 = Calcular o produto que mais faturou (Em Faturamento).
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
display(tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False))

#Passo6 = Calcular loja/cidade que mais vendeu (Em Faturamento).
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
display(tabela_lojas)

#Passo7 = Criar grafico passo 6.
grafico = tabela_lojas.plot (kind='bar')
plt.show()