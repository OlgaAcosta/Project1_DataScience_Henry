# PROYECTO INDIVIDUAL Nº1

## Machine Learning Operations (MLOps)
Realizado por Olga Acosta

![Imagen MLOps](https://drive.google.com/file/d/1YPBYE35nQGHmN1sYdr0R5mq14ZzsV4uj/view?usp=sharing)

## Introducción
Este proyecto corresponde al primero de la etapa de "Lab's" del programa de Data Science de Henry. El rol a desempeñar es el de MLOps Engineer.

![Logo Henry]((https://images.app.goo.gl/HQUovVYKeWLs85oh7)

## Contexto de los datos
Los datos a partir de los cuales se desarrolló el proyecto fueron dos archivos CSV: "movies_dataset.csv" y "credits.csv".

Datasets otorgados: [Enlace a los datasets](https://drive.google.com/drive/folders/1qyq-didCwr35Q9m2BOByNjYOf4rSQiYu?usp=sharing)

Diccionario del dataset "movies_dataset.csv": [Enlace al diccionario](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0)

## Propuesta de trabajo

![Flujo de trabajo](https://raw.githubusercontent.com/HX-PRomero/PI_ML_OPS/main/src/DiagramaConceptualDelFlujoDeProcesos.png)

### ETL
- Desanidar datos de diversos campos.
- Revisión, manejo e imputación de nulos.
- Transformaciones de tipo de dato en diversos campos.
- Creación de nuevas columnas con datos relevantes y normalizados.
- Unión de datasets.
- Eliminación de columnas innecesarias.
- Exportación de los datos transformados a un nuevo CSV.

Se puede revisar el paso a paso documentado de este proceso en el siguiente link: [Notebook ETL](https://colab.research.google.com/drive/1kWI6LmHgVvF1Axcs9qryPazZhp4iir5l?usp=sharing)

### EDA
- Obtención de correlaciones de las variables numéricas.
- Generación de pairplots e histogramas de ciertas variables.
- Detección de patrones.
- Análisis de correlaciones y distribuciones.
- Eliminación de datos con poca influencia o poco útiles.
- Realización de word clouds para descubrir las palabras más frecuentes.
- Elección de las variables para el modelo de Machine Learning.
- Exportación de los datos finales a un nuevo CSV.

Se puede revisar el paso a paso documentado de este proceso en el siguiente link: [Notebook EDA](https://colab.research.google.com/drive/1CUi06VKs2fPI5aYu0TVrDLV81uMahyCl?usp=sharing)

### Machine-learning
- Filtrar el dataset a partir de los géneros del título ingresado.
- Vectorizar los campos de interés "title" y "overview".
- Obtener la similitud de coseno entre el título ingresado y los demás a partir de sus vectores.
- Comparar los índices de similitud y obtener las cinco más similares.
- Crear un diccionario con los datos correspondientes a las cinco películas elegidas.

Se puede revisar el paso a paso documentado del proceso de EDA y ML en el siguiente link: [Notebook ML](https://colab.research.google.com/drive/1CUi06VKs2fPI5aYu0TVrDLV81uMahyCl?usp=sharing)

## Resultado

![Resultado](https://drive.google.com/file/d/1wq-ZL8w0ez1-TQw9jTI1JCb13EeEu0UB/view?usp=drive_link)

El resultado final consiste en una API renderizada con las siete funciones requeridas.

Se puede acceder a ella en el siguiente link: [API](https://henry-project1-olgaacosta.onrender.com/docs)

Se puede revisar el paso a paso documentado de las siete funciones en el siguiente link: [Notebook Funciones](https://colab.research.google.com/drive/1usjeb39-Xt_gEezP5dp_tWLvdG8d6Xr_?usp=sharing)

## Herramientas utilizadas

![Python](ruta_de_imagen_python.jpg)
![Scikit-Learn](ruta_de_imagen_scikitlearn.jpg)
![Pandas](ruta_de_imagen_pandas.jpg)
![NumPy](ruta_de_imagen_numpy.jpg)
![Matplotlib](ruta_de_imagen_matplotlib.jpg)
![FastAPI](ruta_de_imagen_fastapi.jpg)
![Render API](ruta_de_imagen_render_api.jpg)


