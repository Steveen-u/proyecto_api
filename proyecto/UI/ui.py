
        
def ingresar_datos():
    # Pide al usuario que ingrese el nombre del departamento y el número límite de registros
    nombre_departamento = input("Ingrese el nombre del departamento: ").upper()
    limite_registros = int(input("Ingrese el número límite de registros: "))
    # retornamos el nombre del departamento que se quiere ver junto al limite de registros
    return nombre_departamento, limite_registros
    
def mostrar_resultados( data):
    # Muestra los resultados en un formato legible para el usuario
    columnas = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_procedencia']
    print(data[columnas])