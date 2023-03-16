from UI import ui
from API import api

def main():
    
    
    # Obtiene los datos de entrada del usuario
    nombre_departamento, limite_registros = ui.ingresar_datos()
    
    # Obtiene los datos de COVID-19 del API
    data = api.obtener_datos(nombre_departamento, limite_registros)
    
    # Muestra los resultados al usuario
    ui.mostrar_resultados(data)


main()