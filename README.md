<p align="center">
  <h1>PROYECTO INDIVIDUAL Nº1</h1>
</p>

<p align="center">
  <img src="https://e17r5k-datap1.s3-eu-west-1.amazonaws.com/evercorp-empleo-blog/s3fs-public/mlops-versionado-de-modelos_0.png" alt="Imagen MLOps">
  <h2>Machine Learning Operations (MLOps)</h2>
  <em>Realizado por Olga Acosta</em>
</p>

<p align="center">
  <img src="https://assets.soyhenry.com/henry-landing/assets/Henry/logo.png" alt="Logo Henry">
</p>

## Introducción
Este proyecto corresponde al primero de la etapa de *Lab's* del programa de **Data Science** de **Henry**. El rol a desempeñar es el de MLOps Engineer.

## Contexto de los datos
Los datos a partir de los cuales se desarrolló el proyecto fueron dos archivos en formato csv: *movies_dataset.csv* y *credits.csv*.

- Datasets otorgados: [Enlace a los datasets](https://drive.google.com/drive/folders/1qyq-didCwr35Q9m2BOByNjYOf4rSQiYu?usp=sharing)
- Diccionario del dataset *movies_dataset.csv*: [Enlace al diccionario](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0)

## Propuesta de trabajo

<p align="center">
  <img src="https://raw.githubusercontent.com/HX-PRomero/PI_ML_OPS/main/src/DiagramaConceptualDelFlujoDeProcesos.png" alt="Flujo de trabajo">
</p>

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

Se puede revisar el paso a paso documentado del proceso de ML en la sección final del siguiente link: [Notebook ML](https://colab.research.google.com/drive/1CUi06VKs2fPI5aYu0TVrDLV81uMahyCl?usp=sharing)

## Resultado

<p align="center">
  <img src="https://github.com/OlgaAcosta/Project1_DataScience_Henry/blob/main/src/imagen%20fastapi%20final.jpeg" alt="Resultado">
</p>

El resultado final consiste en una API renderizada con las siete funciones requeridas.

Se puede acceder a ella en el siguiente link: [API](https://henry-project1-olgaacosta.onrender.com/docs)

Se puede revisar el paso a paso documentado de las siete funciones en el siguiente link: [Notebook Funciones](https://colab.research.google.com/drive/1usjeb39-Xt_gEezP5dp_tWLvdG8d6Xr_?usp=sharing)

## Herramientas utilizadas

- Python
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- FastAPI
- Render API



