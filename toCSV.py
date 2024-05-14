import pandas as pd
import chardet

# Define os nomes das colunas
columns_names = ['Nome', 'Tipo', 'Numero', 'Codigo', 'Valor']

# Read the file using chardet
rawdata = open("Clientes.txt", "rb").read()
encoding = chardet.detect(rawdata)["encoding"]

# Read the file using the detected encoding
dados = pd.read_csv("Clientes.txt", sep=",", names=columns_names, encoding=encoding)

dados = dados.drop(["Tipo","Valor"], axis=1)
# Salva o DataFrame como um arquivo Excel
dados.to_csv("Contatos.csv", index=False)

