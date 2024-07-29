#!/usr/bin/env python
# coding: utf-8

# # Hola Jenniffer!
# 
# Mi nombre es David Bautista, soy code reviewer de TripleTen y voy a revisar el proyecto que acabas de desarrollar.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres.**
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div
# 
# ¡Empecemos!

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General 
# 
# Hola, Jennifer, te felicito por el desarrollo del proyecto hasta el momento. Ahora bien, he dejado algunos comentarios para que los puedas tener en cuenta para la siguiente entrega. </div>

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Jennifer, no olvides generar una sección de introducción del proyecto. Recuerda que como científico de datos debemos lograr comentar de manera los objetivos e intenciones de nuestros proyectos. 
# </div>

# # Introducción
# 
# El objetivo de este proyecto es realizar un análisis exploratorio de datos y una prueba de hipótesis utilizando datos de la plataforma Zuber. En particular, analizaremos datos de empresas de taxis y viajes en Chicago para identificar patrones y comportamientos. Además, probaremos la hipótesis sobre la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare en días lluviosos comparados con días no lluviosos, específicamente los sábados.
# 

# # Paso 4. Análisis exploratorio de datos (Python)

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Perfecto, buen trabajo importando las librerías necesarias para el desarrollo del proyecto. 
# </div>

# In[10]:


df_company = pd.read_csv('/datasets/project_sql_result_01.csv')
df_company.head() 


# In[11]:


df_company.info()


# In[13]:


df_dropoff= pd.read_csv('/datasets/project_sql_result_04.csv')
df_dropoff.head()


# In[14]:


df_dropoff.info()


# Los tipos de datos en ambos dataframes son correctos, por lo que no es necesario hacer ningún tipo de cambios.
# - company_name y dropoff_location como tipo object,
# - trips_amount como int,
# - average_trips como float

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con la carga y exploración inicial de estas dos tablas. </div>

# In[16]:


# Ordenar los barrios por promedio de viajes y obtener los 10 primeros
top_10_barrios = df_dropoff.sort_values(by='average_trips', ascending=False).head(10)
print(top_10_barrios)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo estructurando la tabla. </div>

# In[17]:


# Gráfico de los 10 barrios principales por número de finalizaciones
plt.figure(figsize=(12, 6))
plt.bar(top_10_barrios['dropoff_location_name'], top_10_barrios['average_trips'], color='skyblue')
plt.title('Top 10 Barrios por Promedio de Viajes')
plt.xlabel('Barrio')
plt.ylabel('Promedio de Viajes')
plt.xticks(rotation=45, ha='right')
plt.show()


# A partir del gráfico de barras podemos identificar los barrios más frecuentados por los taxis, como son Loop, River North y Streeterville. Este tipo de análisis  puede ayudar a entender patrones de movilidad y demanda en diferentes áreas de la ciudad.

# In[21]:


# Gráfico de empresas de taxis y número de viajes
plt.figure(figsize=(12, 6))
plt.bar(top_10_companies['company_name'], top_10_companies['trips_amount'], color='green')
plt.title('Top 10 Compañías de Taxis por Número de Viajes')
plt.xlabel('Compañía de Taxis')
plt.ylabel('Número de Viajes')
plt.xticks(rotation=45, ha='right')
plt.show()

# Limitar a las 10 principales empresas de taxis
top_10_companies = df_company.sort_values(by='trips_amount', ascending=False).head(10)


# El gráfico nos muestra cuáles compañías de taxis realizaron más viajes durante el período estudiado, esto puede indicar la popularidad o la disponibilidad de las compañías en la ciudad, siendo Flash Cab, Taxi Affiliation Services y Medallion Leasing las que más viajes realizaron.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con el desarrollo de las dos gráficas Jennifer, Solamente te recomiendo en el segundo gráfico limitar las observaciones a 10, lo anterior buscando obtener un gráfico más estético . </div>

# # Paso 5. Prueba de hipótesis (Python)

# In[53]:


saturday_trips = pd.read_csv('/datasets/project_sql_result_07.csv')
print(df_trips.head())


# - Hipótesis nula (H0): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare no cambia los sábados lluviosos.
# - Hipótesis alternativa (H1): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.

# In[24]:


saturday_trips['start_ts'] = pd.to_datetime(saturday_trips['start_ts'])

# Dividir los datos entre días lluviosos y no lluviosos
rainy_saturdays = saturday_trips[saturday_trips['weather_conditions'] == 'Bad']
non_rainy_saturdays = saturday_trips[saturday_trips['weather_conditions'] != 'Bad']

# Extraer la duración de los viajes en segundos
rainy_durations = rainy_saturdays['duration_seconds']
non_rainy_durations = non_rainy_saturdays['duration_seconds']


# In[25]:


# Comparar las varianzas
var_rainy = np.var(rainy_durations, ddof=1)
var_non_rainy = np.var(non_rainy_durations, ddof=1)
print(f"Varianza de días lluviosos: {var_rainy}")
print(f"Varianza de días no lluviosos: {var_non_rainy}")


# In[26]:


# Realizar la prueba t de dos muestras independientes
t_stat, p_value = stats.ttest_ind(rainy_durations, non_rainy_durations, equal_var=False)

alpha = 0.05

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula. La duración promedio de los viajes cambia los sábados lluviosos.")
else:
    print("No podemos rechazar la hipótesis nula. La duración promedio de los viajes no cambia los sábados lluviosos.")


# Para probar estas hipótesis, utilizamos una prueba T para dos muestras independientes. Esta prueba es adecuada cuando queremos comparar las medias de dos grupos independientes y determinar si hay evidencia estadística significativa de que sus medias poblacionales son diferentes.Las varianzas de los dos grupos fueron diferentes, por lo cual usamos la prueba t con ajuste para varianzas desiguales. El valor p obtenido fue significativamente menor que el nivel de significancia de 0.05, lo que nos llevó a rechazar la hipótesis nula.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con el desarrollo de la sección de prueba de hipótesis, lo único que te recomiendo es poder desarrollar un análisis comparativo de las varianzas de los dos grupos, lo anterior teniendo en cuenta que es un componente que se deberia fijar como un argumento dentro de la prueba. </div>

# # Conclusiones:
# 
# Los resultados de la prueba indican que hay una diferencia significativa en la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare en días lluviosos comparado con días no lluviosos, específicamente los sábados los viajes tienden a ser más largos. Esta información puede ser útil para planificar y gestionar mejor los recursos de transporte en días lluviosos.
