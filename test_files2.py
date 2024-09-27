
# Abre archivo con manejo de excepción
try:
    
    # Crea archivo my_data.txt
    #file=open('C:\\Users\\samae\\Documents\\docencia-uq\\II-2024\\Programming\\slides\\lecture-1-sources\\my_data.txt','xt')
    file=open('..\\my_data.txt','xt')


    # Solicita texto al usuario
    question=input('Ingrese su pregunta:')

    # Escribe texto en el archivo
    file.write(question)

    # Cierra el archivo
    file.close()

except:
    # El bloque except se ejecuta si hay 
    # excepción, el archivo ya existe
    print('El archivo ya existe')


