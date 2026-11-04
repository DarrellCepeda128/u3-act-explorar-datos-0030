import pandas as pd
import os
## Cepeda Darrell NC = 0030   Fecha 4/11/2026
# URL del dataset público para leer datos de Iris.csv
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)
# print(datos)
# Guardar una copia local
datos.to_csv("datasets/iris.csv", index=False)
# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head()) # muestra las primeras 5 lineas
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print("Monstrando Nombre de las Columnas")
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())
print("\\nINFORMACION DEL DATASET (conjunto de datos)")
print(datos.info())
print("\\nCARACTERISTICAS (X) tumba la columna especies con drop")
X = datos.drop(columns=["species"])
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print("\\nESPECIES REGISTRADAS con la opcion unica")
print(y.unique())
print("Programa ejecutado por Cepeda Darrell NC = 0030")