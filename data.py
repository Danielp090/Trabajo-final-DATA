import pandas as pd
import seaborn as sns
import plotly.express as px
url=("Medicaldataset.csv")
df= pd.read_csv(url)
#df.info()
#eliminacion de valores nulos
df.dropna(inplace=True)
#eliminacion de duplicados
df.drop_duplicates(inplace=True)
#df.info()
#Renombrar columnas
df.rename(columns={"Age":"Edad",
                   "Gender":"Genero",
                   "Heart rate":"Frecuencia cardiaca",
                   "Systolic blood pressure":"Presion arterial sistolica",
                   "Diastolic blood pressure":"Presion arterial diastolica",
                   "Blood sugar":"Azucar en sangre",
                   "Result":"Resultado"}, inplace=True)
#df.info()
#Tratado de atipicos
def remover_atipicos(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    limite_inf = Q1 - 1.5 * IQR
    limite_super = Q3 + 1.5 * IQR
    return df[(df[column] >= limite_inf) & (df[column] <= limite_super)]
# Se crea un dataset nuevo para ver las diferencias entre los datos originales y los filtrados
df_filtrado = df.copy()
df_filtrado = remover_atipicos(df_filtrado, 'Frecuencia cardiaca')
df_filtrado = remover_atipicos(df_filtrado, 'Presion arterial sistolica')
df_filtrado = remover_atipicos(df_filtrado, 'Presion arterial diastolica')
df_filtrado = remover_atipicos(df_filtrado, 'Azucar en sangre')
df_filtrado.info()

