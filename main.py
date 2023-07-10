import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Obtengo los datos en un dataframe:
df_movies = pd.read_csv("datasets\movies.csv", sep=",")
df_movies.info()

# FUNCIÓN 1:
def peliculas_idioma(idioma: str):
    """Recibe por parámetro un idioma (string) y devuelve un diccionario con la cantidad de películas
    producidas en ese idioma. Si el valor ingresado no es string o no se encuentra en los datos,
    devuelve un diccionario con el error correspondiente."""

    #Obtener una lista con los nombres de los idiomas sin repetirlos
    languages_list = list(df_movies["original_language"].unique())

    # Verifico si es string
    try:
        if not isinstance(idioma, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string."})

        # Si el idioma se encuentra en la lista:
        if idioma in languages_list:
            # Creo un data frame con todas las películas en ese idioma:
            df_language = df_movies[df_movies["original_language"] == idioma]
            # Cuento las filas del dataframe:
            movies_count = df_language.shape[0]
            # Retorno la cantidad:
            return {idioma: f"{movies_count} peliculas"}

        # Si el idioma no es´ta en la lista:
        else:
            return {"Error": f"No se encontró ninguna película estrenada en idioma ´{idioma}´"}
        
    # Devuelvo error si no es string
    except ValueError as e:
        # Si no es un string devuelvo "error":
        return e
    

# FUNCIÓN 2:    
def peliculas_duracion(pelicula: str):
    """Recibe por parámetro una pelicula (string) y devuelve un diccionario con la duracion y el año. 
    Si encuentra más de una película con el mismo nombre, devuelve los datos para cada una de ellas.
    Si el valor ingresado no es string o no se encuentra en los datos, devuelve un diccionario con el 
    error correspondiente."""
    
    # Verifico si es string
    try: 
        if not isinstance(pelicula, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string"})
        
        # Normalizo el título
        pelicula=pelicula.strip().title()
        # Filtro el df por el título
        peliculas_filtradas = df_movies[df_movies["title"].str.title() == pelicula]
        
        # Verifico si se encontraron películas con ese título
        if peliculas_filtradas.empty:
            return {"Error": f"No se encontró la película {pelicula}"}

        # Itero sobre las filas filtradas y obtengo la duración y el año de cada una
        resultados = []
        for index, row in peliculas_filtradas.sort_values('release_year').iterrows(): #Ordenar películas por el año
            duracion = row["runtime"]
            año = row["release_year"]
            resultado = {"Duración": duracion, "Año": año}
            resultados.append(resultado)

        # Devuelvo los resultados como una lista de strings
        return {pelicula: resultados}

    # Devuelvo error si no es string
    except ValueError as e:
        return str(e)


# FUNCIÓN 3:

def franquicia(franquicia: str):
    """Recibe por parámetro una franquicia (string) y devuelve un diccionario con la cantidad de peliculas,
    ganancia total y promedio. Si el valor ingresado no es string o no se encuentra en los datos, devuelve 
    un diccionario con el error correspondiente."""
    
    # Valido si se ingresa un string
    try:
        if not isinstance(franquicia, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string"})
        
        # Normalizo el título
        franquicia = franquicia.strip().title()
        
        # Filtro las filas del data frame que coincidan con el nombre de la franquicia
        df_franquicia = df_movies[df_movies["franquicia"].str.title()== franquicia]

        # Valido si se encontraron franquicias con ese nombre
        if df_franquicia.empty:
            return {"Error": f"No se encontró la franquicia {franquicia}"}

        # Defino las variables a devolver
        cantidad= len(df_franquicia)
        gananciaTotal = df_franquicia["revenue"].sum()
        ganaciaPromedio = df_franquicia["revenue"].mean()
        return {franquicia: {"peliculas": cantidad, "ganancia": gananciaTotal, "ganancia promedio": ganaciaPromedio}}

    # Devuelvo error si no es string
    except ValueError as e:
        return str(e)
    

# FUNCIÓN 4:
def peliculas_pais(pais: str):
    """Recibe por parámetro un país (string) y devuelve un diccionario con la cantidad de peliculas producidas
    en el mismo. Si el valor ingresado no es string o no se encuentra en los datos, devuelve un diccionario 
    con el error correspondiente."""
    
    # Valido si se ingresa un string
    try:
        if not isinstance(pais, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string."})

        # Normalizo el pais ingresado
        pais= pais.strip().title()

        # Filtro las filas del dataframe que coincidan con el nombre del pais
        df_pais= df_movies[df_movies['production_countries'].str.title().apply(lambda countries: pais in countries)]

        # Valido si se encontró el pais
        if df_pais.empty:
            return {"Error":f"No se encontró el país {pais}"}
        
        # Defino la variable a devolver
        cantidad= len(df_pais)
        return {pais:f"{cantidad} peliculas"}

    # Devuelvo error si no es string
    except ValueError as e:
        return str(e)
    
    
# FUNCIÓN 5:

def productoras_exitosas( productora : str ):
    """Recibe por parámetro una productora (string) y devuelve un diccionario con el revenue total y la cantidad
    de peliculas que realizó. Si el valor ingresado no es string o no se encuentra en los datos, devuelve un 
    diccionario con el error correspondiente."""
    
    # Valido si se ingresa un string
    try:
        if not isinstance(productora, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string."})

        #Normalizo la productora ingresada
        productora=productora.strip().title()

        # Filtro las filas del dataframe que coincidan con el nombre de la productora
        df_productoras= df_movies[df_movies["production_companies"].str.title().apply(lambda productoras: productora in productoras)]

        # Valido si se encontró la productora
        if df_productoras.empty:
            return {"Error":f"No se encontró la productora {productora}"}

        # Defino cantidad de peliculas y el revenue total
        cantidad= len(df_productoras)
        revenue_total= df_productoras["revenue"].sum()
        return {productora: [f"$ {revenue_total}", f"{cantidad} peliculas"]}
    
    # Devuelvo error si no es string
    except ValueError as e:
        return str(e)
    
    
# FUNCIÓN 6:

def get_director( nombre_director: str ):
    """Recibe por parámetro un director (string) y devuelve un diccionario la suma del revenue. Además, devuelve
    el nombre de cada película dirigida con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, 
    en formato lista. Si el valor ingresado no es string o no se encuentra en los datos, devuelve un diccionario 
    con el error correspondiente."""
    
    # Valido si se ingresa un string
    try:
        if not isinstance(nombre_director, str):
            raise ValueError({"Error":"Tipo de dato debe ser un string."})

        # Normalizo la productora ingresada
        nombre_director=nombre_director.strip().title()

        # Filtro el dataframe que coincida con el nombre del director
        df_directors= df_movies[df_movies["director"].str.title().apply(lambda directors: nombre_director in directors)]

        # Valido si se encontró la productora
        if df_directors.empty:
            return {"Error":f"No se encontró el director {nombre_director}"}

        # Defino el retorno, los nombres de las películas y la fecha
        director_success = df_directors['revenue'].sum()
        director_movies = []

        # Recorro el dataframe df_directors para obtener la info de cada una de sus peliculas
        for index, row in df_directors.iterrows():
            movie_info = {
                'titulo': row['title'],
                'fecha lanzamiento': row['release_date'],
                'retorno': row['return'],
                'costo': row['budget'],
                'recaudación': row['revenue']
            }
            director_movies.append(movie_info)

        return {"recaudación total": director_success, "películas": director_movies}

    # Devuelvo error si no es string
    except ValueError as e:
        return str(e)
    
    
# FUNCIÓN 7:
def recomendacion(titulo: str):
    """Recibe por parámetro una película (string) y devuelve un diccionario con cinco recomendaciones de peliculas
    en orden de similitud, junto a sus género y vote_average. Si encuentra más de una película con el mismo nombre,
    devuelve recomendaciones para cada una, diferenciándolas por el año. Si el valor ingresado no es string o no se 
    encuentra en los datos, devuelve un diccionario con el error correspondiente."""
    
    movies= pd.read_csv("datasets\ml_movies.csv")

  # Verifico si el titulo es un string:
    if type(titulo)!= str:
        return {"Error": f"'{titulo}' no es un string"}

    # Si es un string, continúa el código. Normalizo el título:
    titulo = titulo.strip().title()


    # Verifico si el título se encuentra en el dataframe:
    if movies[movies['title'].str.title() == titulo].shape[0] == 0:
        return {"Error": f"No se encontró la película {titulo}"}

    # Si se encuentra en el dataframe, creo un nuevo df con todas las películas con el mismo título:
    movies_same_title = movies[movies['title'].str.title() == titulo]

    # Creo el diccionario de recomendaciones finales:
    recommendations_dict = {}

    # Itero en el nuevo df para obtener los datos correspondientes:
    for _, movie in movies_same_title.iterrows():
            movie_title = movie['title'] # Obtengo cada título
            movie_anio = movie['release_year'] # Obtengo el año
            movie_id = movie['id'] # Obtengo el id de cada película
            movie_genre = ast.literal_eval(movie["genres"]) # Obtengo los géneros convirtiéndolos a lista

            # Verifico que tenga al menos un género registrado:
            if len(movie_genre) == 0:
                return {"Error": f"No se encontraron recomendaciones para la película {titulo}"}

            # Si tiene al menos un género, continúa el código:
            else:
                # Un solo género: filtro el df con películas de solo un género y que sea el mismo:
                if len(movie_genre) == 1:
                    filtered_movies = movies[movies['genres'].apply(lambda x: len(ast.literal_eval(x)) == 1 and ast.literal_eval(x) == movie_genre)]

                # Dos géneros: filtro el df con películas de solo dos géneros, que sean los mismos y en el mismo orden:
                elif len(movie_genre) == 2:
                    filtered_movies = movies[movies['genres'].apply(lambda x: len(ast.literal_eval(x)) == 2 and ast.literal_eval(x)== movie_genre)]

                # Tres géneros: filtro el df con películas de solo tres géneros, que sean los mismos y en el mismo orden:
                elif len(movie_genre) == 3:
                    filtered_movies = movies[movies['genres'].apply(lambda x: len(ast.literal_eval(x)) >= 3 and ast.literal_eval(x)[:3] == movie_genre[:3])]

                # Más de tres géneros: filtro el df con películas de al menos tres géneros, que coincidan en el orden de los tres primeros:
                else:
                    filtered_movies = movies[movies['genres'].apply(lambda x: len(ast.literal_eval(x)) >= 3 and ast.literal_eval(x)[:3] == movie_genre[:3])]


                # Reseteo el índice del dataframe filtrado para no tener problemas en encontrar los índices de las coincidencias:
                filtered_movies = filtered_movies.reset_index(drop=True)

                # Creo un vectorizador TF-IDF para las características de las películas (title y overview):
                tfidf = TfidfVectorizer(stop_words='english')

                # Combino las características (title y overview) en un solo campo:
                filtered_movies['combined_features'] = filtered_movies['title'] + ' ' + filtered_movies['overview'].fillna('') # Imputo nulos en "overview"

                # Calculo la matriz TF-IDF de las características:
                tfidf_matrix = tfidf.fit_transform(filtered_movies['combined_features'])

                # Busco el índice correspondiente al ID de la película ingresada:
                movie_index = filtered_movies[filtered_movies['id'] == movie_id].index[0]

                # Calculo la similitud de coseno entre la película de entrada y las películas filtradas:
                similarities = cosine_similarity(tfidf_matrix[movie_index], tfidf_matrix).flatten()

                # Obtengo los índices de las 5 películas más parecidas (excluyendo la película ingresada):
                top_indices = similarities.argsort()[-6:-1][::-1]

                # Creo el diccionario de recomendaciones para el título correspondiente a la iteración actual:
                recommendations = {}
                for idx in top_indices:
                    rec_movie_title = filtered_movies.iloc[idx]['title']
                    rec_movie_genres = filtered_movies.iloc[idx]['genres']
                    rec_movie_vote_average = filtered_movies.iloc[idx]['vote_average']
                    recommendations[rec_movie_title] = {'generos': rec_movie_genres, 'puntaje': rec_movie_vote_average}

                # Lleno el diccionario final con las recomendaciones de la iteración actual:
                recommendations_dict[f"{movie_title}, año {movie_anio}"] = recommendations

    # Devuelvo el diccionario final que contiene recomendaciones para cada película que coincida con el título ingresado:
    return recommendations_dict


