import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url=("Medicaldataset.csv")
df= pd.read_csv(url)
#df.info()
#eliminacion de valores nulos
df.dropna(inplace=True)
#eliminacion de duplicados
df.drop_duplicates(inplace=True)
df.info()
