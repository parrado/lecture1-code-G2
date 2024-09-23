# Ejemplo de diccionarios y conjuntos

from random import choice

# Lista de dos preguntas
# cada elemento es un diccionario
# la clave "answers" es una lista de cadenas
questions=[
    {
    "statement":"Name of creator of Python:",
    "answers":["A. Guido","B. Dennis","C. Bjarne","D. Linus"],
    "key":"A"
},
    {
    "statement":"Birth year of stephen hawking",
    "answers":["A. 1939","B. 1896","C. 1942","D. 1912"],
    "key":"C"
}

]

# Crea un conjunto vacío para
# las preguntas correctas
rightAnswer=set()

# Elige pregunta aleatorio 
# usando la función choice
question=choice(questions)

# Imprime la pregunta
print(question["statement"])
for a in question["answers"]:
    print(a)

# Solicita la opción de respuesta
# al usuario y la convierte a mayúscula
option=input("Select your answer: A, B, C or D").upper()

# Si responde correctamente
if option==question["key"]:
    # Añade la pregunta correcta al conjunto
    rightAnswer.add(question["statement"])

# Imprime el conjunto con la pregunta correcta
print(rightAnswer)

for item in rightAnswer:
    print(item)
