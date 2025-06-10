import streamlit as st
import pandas as pd
import plotly.express as px
from data import *
st.title("Análisis de Datos Médicos")
st.header("Introducción")
st.write("Este es un análisis de un conjunto de datos médicos que incluye información sobre la edad, género, frecuencia cardiaca, presión arterial, azúcar en sangre y resultados de pruebas médicas.")
# Cargar el dataset
st.write(df.head())
#Filtrado del dataset por rango de edades con toggle
st.toggle("Filtrar por rango de edades", key="toggle_age_filter")
if st.session_state.toggle_age_filter:
    min_edad = st.slider("Edad mínima", int(df['Edad'].min()), int(df['Edad'].max()), int(df['Edad'].min()))
    max_edad = st.slider("Edad máxima", int(df['Edad'].min()), int(df['Edad'].max()), int(df['Edad'].max()))
    df_filt = df[(df['Edad'] >= min_edad) & (df['Edad'] <= max_edad)]
    st.write(f"Datos filtrados por edad entre {min_edad} y {max_edad}:")
    st.write(df_filt.head())
#Matriz de correlación
st.toggle("Matriz de Correlación", key="toggle_corr_matrix")
if st.session_state.toggle_corr_matrix:
    st.subheader("Matriz de Correlación")
    fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto")
    st.plotly_chart(fig_corr)
    st.toggle("Resumen de la Matriz de Correlación", key="toggle_corr_summary")
    if st.session_state.toggle_corr_summary:
        st.write("La matriz muestra que las presiones arteriales sistólica y diastólica están moderadamente correlacionadas positivamente. Otras relaciones, como entre la frecuencia cardíaca y la presión diastólica, o entre la edad y la troponina, son más débiles. Muchas de las variables presentan correlaciones muy bajas entre sí, indicando poca relación lineal directa.")
# Gráficos de dispersión
st.toggle("Gráficos de Dispersión", key="toggle_scatter_plots")
if st.session_state.toggle_scatter_plots:
    st.subheader("Gráficos de Dispersión")
    fig1 = px.scatter(df_filtrado, x="Edad", y="Frecuencia cardiaca", title="Frecuencia Cardiaca vs Edad")
    st.plotly_chart(fig1)
    st.write("La gráfica muestra que los individuos presentan frecuencias cardíacas que mayormente oscilan entre 40 y 120 latidos por minuto, a lo largo de un amplio rango de edades. No se observa una correlación lineal fuerte o evidente entre la edad y la frecuencia cardíaca, destacándose una considerable variabilidad individual en todos los grupos de edad.")

    fig2 = px.scatter(df_filtrado, x="Presion arterial sistolica", y="Presion arterial diastolica", title="Presión Arterial Sistolica vs Diastolica")
    st.plotly_chart(fig2)
    st.write("La gráfica muestra una clara correlación positiva entre la presión arterial sistólica y la presión arterial diastólica. A medida que una aumenta, la otra también tiende a hacerlo. Los datos se distribuyen en una nube ascendente, con la mayoría de las presiones sistólicas entre aproximadamente 100-160 mmHg y las diastólicas entre 60-90 mmHg, aunque con una notable variabilidad individual alrededor de esta tendencia general.")

    fig3 = px.scatter(df_filtrado, x="Azucar en sangre", y="Frecuencia cardiaca", title="Azúcar en Sangre vs Frecuencia Cardiaca")
    st.plotly_chart(fig3)
    st.write("La gráfica muestra los niveles de azúcar en sangre versus la frecuencia cardíaca. Los datos presentan una gran dispersión, sin una correlación lineal fuerte o evidente entre ambas variables. Para la mayoría de los niveles de azúcar en sangre registrados (principalmente entre 80-150 mg/dL) y frecuencias cardíacas (principalmente entre 60-100 lpm), se observa una amplia variabilidad, lo que sugiere que estos dos factores tienen una relación lineal débil o inexistente en este conjunto de datos.")

    fig4 = px.scatter(df_filtrado, x="Edad", y="Azucar en sangre", title="Azúcar en Sangre vs Edad")
    st.plotly_chart(fig4)
    st.write("La gráfica muestra una amplia dispersión de los niveles de azúcar en sangre (mayormente entre 50 y más de 250 mg/dL) a lo largo de un extenso rango de edades (aproximadamente de 20 a 100 años). No se observa una correlación lineal fuerte o evidente entre la edad y el nivel de azúcar en sangre. La característica principal es la considerable variabilidad de los niveles de azúcar en sangre en todos los grupos de edad, lo que sugiere una relación lineal débil o inexistente entre estas dos variables en el conjunto de datos.")
    fig5 = px.scatter(df_filtrado, x="Presion arterial sistolica", y="Azucar en sangre", title="Azúcar en Sangre vs Presión Arterial Sistolica")
    st.plotly_chart(fig5)
    st.write("La gráfica muestra una amplia dispersión de los niveles de azúcar en sangre (mayormente entre 50 y más de 250 mg/dL) frente a un extenso rango de valores de presión arterial sistólica (principalmente entre 90-160 mmHg). No se observa una correlación lineal fuerte o evidente entre estas dos variables. La característica principal es la considerable variabilidad de los niveles de azúcar en sangre para cualquier nivel de presión arterial sistólica dado (y viceversa), lo que sugiere una relación lineal débil o inexistente entre estos dos factores en el conjunto de datos.")
    fig6 = px.scatter(df_filtrado, x="Presion arterial diastolica", y="Azucar en sangre", title="Azúcar en Sangre vs Presión Arterial Diastolica")
    st.plotly_chart(fig6)
    st.write("La gráfica muestra una amplia dispersión de los niveles de azúcar en sangre (mayormente entre 50 y más de 250 mg/dL) frente a un extenso rango de valores de presión arterial diastólica (principalmente entre 50-100 mmHg). No se observa una correlación lineal fuerte o evidente entre estas dos variables. La característica principal es la considerable variabilidad de los niveles de azúcar en sangre para cualquier nivel de presión arterial diastólica dado (y viceversa), lo que sugiere una relación lineal débil o inexistente entre estos dos factores en el conjunto de datos.")
#Pruebas de normalidad
st.toggle("Pruebas de Normalidad", key="toggle_normality_tests")
if st.session_state.toggle_normality_tests:
    st.subheader("Pruebas de Normalidad")
    resultados_pruebas_normalidad = pruebas_normalidad(df_filtrado)
    resultados_df = pd.DataFrame(resultados_pruebas_normalidad).T
    st.write(resultados_df)
    st.write("Los resultados de la prueba de normalidad muestran que la mayoría de las variables no siguen una distribución normal, con valores p generalmente inferiores a 0.05, lo que indica que se rechaza la hipótesis nula de normalidad para estas variables.")
#Pruebas de Pearson
st.toggle("Pruebas de Pearson", key="toggle_pearson_test")
if st.session_state.toggle_pearson_test:
    #Prueba Pearson entre Edad y Frecuencia Cardiaca
    st.subheader("Prueba de Pearson entre Edad y Frecuencia Cardiaca")
    df_filtrado['Edad'] = df_filtrado['Edad'].astype(int)  
    df_filtrado['Rango Edad'] = (df_filtrado['Edad'] // 10) * 10
    df_filtrado = df_filtrado[df_filtrado['Rango Edad'] < 100]  
    df_filtrado = df_filtrado[df_filtrado['Frecuencia cardiaca'] > 0]
    figcajas = px.box(df_filtrado, x='Rango Edad', y='Frecuencia cardiaca', title='Frecuencia Cardiaca por Rango de Edad')
    st.plotly_chart(figcajas)
    corr, p_value = prueba_pearson(df_filtrado, 'Rango Edad', 'Frecuencia cardiaca')
    st.write(f"Coeficiente de correlación de Pearson: {corr}, Valor p: {p_value}")
    if p_value < 0.05:
        st.write("Existe una correlación significativa entre la edad y la frecuencia cardiaca.")
    else:
        st.write("No existe una correlación significativa entre la edad y la frecuencia cardiaca.")
    st.subheader("Prueba de Pearson entre Edad y Azúcar en Sangre")
    #Grafica de vilones
    df_filtrado['Edad'] = df_filtrado['Edad'].astype(int)  # Asegurar de que la columna Edad sea de tipo entero
    df_filtrado['Rango Edad'] = (df_filtrado['Edad'] // 10) * 10
    figviolines = px.violin(df_filtrado, x='Rango Edad', y='Azucar en sangre', title='Azúcar en Sangre por Rango de Edad')
    st.plotly_chart(figviolines)
    corr, p_value = prueba_pearson(df_filtrado, 'Rango Edad', 'Azucar en sangre')
    st.write(f"Coeficiente de correlación de Pearson: {corr}, Valor p: {p_value}")
    if p_value < 0.05:
        st.write("Existe una correlación significativa entre la edad y el azúcar en sangre.")
    else:
        st.write("No existe una correlación significativa entre la edad y el azúcar en sangre.")
    #Prueba pearson de presion arterial sistólica y diastólica
    st.subheader("Prueba de Pearson entre Presión Arterial Sistolica y Diastolica")
    #grafico scatter
    fig_presion = px.scatter(df_filtrado, x='Presion arterial sistolica', y='Presion arterial diastolica', title='Presión Arterial Sistolica vs Diastolica')
    st.plotly_chart(fig_presion)
    corr, p_value = prueba_pearson(df_filtrado, 'Presion arterial sistolica', 'Presion arterial diastolica')
    st.write(f"Coeficiente de correlación de Pearson: {corr}, Valor p: {p_value}")
    if p_value < 0.05:
        st.write("Existe una correlación significativa entre la presión arterial sistólica y diastólica.")
    else:
        st.write("No existe una correlación significativa entre la presión arterial sistólica y diastólica.")
#Prueba Chi2 de género y resultado
st.toggle("Prueba Chi2", key="toggle_chi2_test")
if st.session_state.toggle_chi2_test:
    st.subheader("Prueba Chi2 entre Género y Resultado")
    #Grafica distribución del género y resultado
    df['Genero'] = df['Genero'].astype('category')  
    df['Resultado'] = df['Resultado'].astype('category')  #Se hace la columna de tipo categorico para estar poder hacer el grafdico
    fig_gen_result = px.histogram(df, x='Genero', color='Resultado', barmode='group', title='Distribución de Género y Resultado')
    st.plotly_chart(fig_gen_result)
    chi2_stat, p_value = prueba_chi2(df, 'Genero', 'Resultado')
    st.write(f"Estadístico Chi2: {chi2_stat}, Valor p: {p_value}")
    if p_value < 0.05:
        st.write("Existe una asociación significativa entre el género y el resultado.")
    else:
        st.write("No existe una asociación significativa entre el género y el resultado.")
#Prueba ANOVA de edad y presión arterial sistólica y diastólica y azúcar en sangre
st.toggle("Pruebas ANOVA", key="toggle_anova_test")
if st.session_state.toggle_anova_test:
    st.subheader("Prueba ANOVA entre Edad y Presión Arterial")
    anova_stat, anova_p_value = prueba_anova(df_filtrado, 'Rango Edad', 'Presion arterial sistolica')
    st.write(f"Estadístico ANOVA: {anova_stat}, Valor p: {anova_p_value}")
    if anova_p_value < 0.05:
        st.write("Existe una diferencia significativa entre los grupos de edad en relación a la presión arterial sistólica.")
    else:
        st.write("No existe una diferencia significativa entre los grupos de edad en relación a la presión arterial sistólica.")
    st.subheader("Prueba ANOVA entre Edad y Presión Arterial Diastólica")
    anova_stat, anova_p_value = prueba_anova(df_filtrado, 'Rango Edad', 'Presion arterial diastolica')
    st.write(f"Estadístico ANOVA: {anova_stat}, Valor p: {anova_p_value}")
    if anova_p_value < 0.05:
        st.write("Existe una diferencia significativa entre los grupos de edad en relación a la presión arterial diastólica.")
    else:
        st.write("No existe una diferencia significativa entre los grupos de edad en relación a la presión arterial diastólica.")
    st.subheader("Prueba ANOVA entre Edad y Azúcar en Sangre")
    anova_stat, anova_p_value = prueba_anova(df_filtrado, 'Rango Edad', 'Azucar en sangre')
    st.write(f"Estadístico ANOVA: {anova_stat}, Valor p: {anova_p_value}")
    if anova_p_value < 0.05:
        st.write("Existe una diferencia significativa entre los grupos de edad en relación al azúcar en sangre.")
    else:
        st.write("No existe una diferencia significativa entre los grupos de edad en relación al azúcar en sangre.")
    st.subheader("Prueba ANOVA entre Género y Frecuencia Cardiaca")
    anova_stat, anova_p_value = prueba_anova(df, 'Genero', 'Frecuencia cardiaca')
    st.write(f"Estadístico ANOVA: {anova_stat}, Valor p: {anova_p_value}")  
    if anova_p_value < 0.05:
        st.write("Existe una diferencia significativa entre los géneros en relación a la frecuencia cardiaca.")
    else:
        st.write("No existe una diferencia significativa entre los géneros en relación a la frecuencia cardiaca.")
#Conclusiones
st.toggle("Conclusiones", key="toggle_conclusions")
if st.session_state.toggle_conclusions:
    st.subheader("Conclusiones")
    st.write("Basándonos en las pruebas y visualizaciones que hemos discutido, se puede concluir que el estudio general sugiere un panorama complejo de interacciones. Si bien múltiples variables fisiológicas continuas examinadas, como la relación entre los niveles de azúcar en sangre y la edad, la frecuencia cardíaca con el azúcar en sangre, o el azúcar en sangre con las diferentes presiones arteriales, no presentaron consistentemente correlaciones lineales fuertes entre sí –indicando una limitada interdependencia directa al analizar estos pares específicos–, esto no disminuye su relevancia individual. De hecho, esta falta de correlaciones directas pronunciadas entre muchos parámetros continuos contrasta notablemente con hallazgos específicos del estudio, como la asociación significativa que se encontró entre el género y el resultado, lo que subraya que variables de diferente naturaleza (en este caso, una categórica como el género) pueden tener una influencia más determinante o un papel explicativo crucial en el resultado final investigado, destacando la importancia de un análisis multifactorial.")
    