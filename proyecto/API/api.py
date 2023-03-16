# invocamos las librerias necesarias para la conexión a la base de datos
from sodapy import Socrata
import pandas as pd

def cliente(): # definimos la función que llama al cliente de la base de datos
    client = Socrata ("www.datos.gov.co", None )
    return client # retornamos el cliente

# definimos la función que obtiene los datos 
def obtener_datos(nombre_departamento, limite_registros): 
    # Obtiene los datos de COVID-19 del departamento y número límite de registros especificados
    results = cliente().get("gt2j-8ykr", departamento_nom=nombre_departamento, limit=limite_registros)
    # transforma los datos en un dataframe para facilitar su visualización
    results_df = pd.DataFrame.from_records(results)
    # como nos piden país de procedencia y en la base de datos no encontramos este dato
    # lo agregamos de forma manual y decimos que imprima " no se encuentra"
    results_df.insert(6,"pais_procedencia","No se encuentra")
        # retorna los resultados ya convertidos en dataframe
    return results_df


