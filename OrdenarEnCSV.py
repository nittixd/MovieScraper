import estructura
import pandas as pd
import csv


"""
ObtenerLinksPorPagina
Se le pasa como parametro una pagina.
Devuelve una lista con los links de las peliculas de esa pagina

recorrerpelis
No tiene ningun parametro
Devuelve una lista con los links de las primeras 10 paginas

GetMoviesDetails
Se le pasa como parametro el URL de una pelicula.
Devuelve un diccinario con la informacion de esa pelicula

PASOS


4- Obtener los detalles de cada pelicula y almacenarlos en la nueva lista.
5- Teniendo una lista con la informacion de todas las peliculas de todos los links, debes guardarlo en un CSV.
"""

Recorrerlos = estructura.recorrerpelis(paginas = 10)

LitaDePeliculas = []

for enlace in (Recorrerlos):
    detalles = estructura.GetMoviesDetails(enlace)
    LitaDePeliculas.append(detalles)
    
GuardarEnPandas = pd.DataFrame(LitaDePeliculas)
GuardarEnPandas.to_csv("csv.csv", index=False)

print(GuardarEnPandas)

