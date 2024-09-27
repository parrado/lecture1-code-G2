
# Abre archivo con manejo de excepción
try:
    # Solicita nombre de archivo al usuario 
    # e intenta abrir para lectura
    file=open(input('Ingrese el nombre del archivo:'))

    # Lee línea del archivo
    question=file.readline()

    # Imprime la línea leída
    print(question)

    # Cierra el archivo
    file.close()
except FileNotFoundError:
    # Si se genera excepción
    print('El archivo no existe')


