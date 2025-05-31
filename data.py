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
#Quitar columnas que no se van a usar
df_filtrado.drop(columns=['Genero', 'Resultado'], inplace=True)

#Matriz de correlacion
correlation_matrix = df_filtrado.corr()
#Pruebas de normalidad
def pruebas_normalidad(data):
    from scipy import stats
    resultados = {}
    for column in data.columns:
        stat, p_value = stats.shapiro(data[column])
        resultados[column] = {'Estadístico': stat, 'valor p': p_value}
    return resultados
resultados_pruebas_normalidad = pruebas_normalidad(df_filtrado)
#Prueba pearson de dos variables
def prueba_pearson(data, var1, var2):
    from scipy.stats import pearsonr
    corr, p_value = pearsonr(data[var1], data[var2])
    return corr, p_value
#Prueba chi2 de dos varuables
def prueba_chi2(data, var1, var2):
    from scipy.stats import chi2_contingency
    contingency_table = pd.crosstab(data[var1], data[var2])
    chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)
    return chi2_stat, p_value
#Prueba anova
def prueba_anova(data, var1, var2):
    from scipy.stats import f_oneway
    groups = [group[var2].values for name, group in data.groupby(var1)]
    stat, p_value = f_oneway(*groups)
    return stat, p_value
