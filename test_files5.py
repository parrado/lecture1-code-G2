# Combinación de bloques try/except con with
try:
    archiveName=input('Ingrese el nombre del archivo:')
    file=open('data/'+archiveName)
    #a=[]
    #print(a[0])
except FileNotFoundError:
    print('El archivo no existe')
except IndexError:
    print('Error de indice')
else:
    with file:
        # Lee todas las líneas del archivo
        # como una lista.
        #lines=file.readlines()
        line=file.readline()
        lines=line.split(',')
        #print(lines)
        for line in lines:
            print(line)
        #for i in range(len(lines)):
        #    print(lines[i])