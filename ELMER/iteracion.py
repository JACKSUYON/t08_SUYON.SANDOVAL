# EJERCICIO 1
# IMPRIMIR ELMER
nombre="ELMER"
for letra in nombre:
    print(letra)

# EJERCICIO 2
# IMPRIMIR TE LLAMO LUEGO HERMANA
mensaje=" TE LLAMO LUEGO HERMANA"
for letra in mensaje:
    print(letra)

# EJERCICIO 3
# CONTAR EL NUMERO DE VOCALES EXITEN "E"
mensaje=" TE ESPERO EN EL PARQUE"
contador=0
for vocales in mensaje:
    if (vocales=="E"):
        contador+=1
print("la cantidad de vocales E:",contador)


# EJERCICIO 4
# CONTAR EL NUMERO DE VOCALES DEL SIGUIENTE MENSAJE
mensaje="YOEL SANDOVAL DE LA CRUZ"
contador1,contador2,contador3,contador4,contador5=0,0,0,0,0
for vocales in mensaje:
    if (vocales=="A"):
        contador1 +=1
    if (vocales=="E"):
        contador2 +=1
    if (vocales=="I"):
        contador3 +=1
    if (vocales=="O"):
        contador4 +=1
    if (vocales=="U"):
        contador5 +=1


print(" la cantidad de vocales A:",contador1)
print(" la cantidad de vocales E:",contador2)
print(" la cantidad de vocales I:",contador3)
print(" la cantidad de vocales O:",contador4)
print(" la cantidad de vocales U:",contador5)


# EJERCICIO 5
# IMPRIMIR JUDAS TADEO
mensaje="JUDAS TADEO"
for letra in mensaje:
    print(letra)


# EJERCICIO 6
# IMPRIMIR "PORQUE LE DIJISTE QUE MAÑANA NO VENIA"
mensaje=" PORQUE LE DIJISTE QUE MAÑANA NO VENIA"
for letra in mensaje:
    print(letra)


# EJERCICIO 7
# BUSCAR LA LETRA O VOCAL DE MAYOR ASIGNACIONES
mensaje=" WHAT IS HIS NAME"
contador=0
for vocales in mensaje:
    if (vocales=="I"):
        contador+=1

print("la cantidad de vocal I es:",contador)


# EJERCICIO 8
# IMPRIMIR 2 VECES EL SIGUIENTE MENSAJE
mensaje=" HELLO MY MOTHER"
for letra in mensaje:
    print(letra)
for letra in mensaje:
    print(letra)



# EJERCICIO 9
# BUSCARL LAS VOCALES
mensaje=" ESTUDIO EN LA UIVERSIDAD PEDRO RUIZ GALLO"
contador1,contador2,contador3,contador4,contador5
for vocales in mensaje:
    if (vocales=="A"):
        contador1 +=1
    if (vocales=="E"):
        contador2 +=1
    if (vocales=="I"):
        contador3 +=1
    if (vocales=="O"):
        contador4 +=1
    if (vocales=="U"):
        contador5 +=1

print("A:",contador1)
print("E:",contador2)
print("I:",contador3)
print("O:",contador4)
print("U:",contador5)


# EJERCICIO 10
# IMPRIMIR "LOS TRIUNFADORES DEL FUTURO"
mensaje="LOS TRIUNFADORES DEL FUTURO"
for letra in mensaje:
    print(letra)

# EJERCICIO 11
# MOSTRAR LOS NUMEROS 1 HASTA AL 9
numeros="1 2 3 4 5 6 7 8 9"
for numero in numeros:
    print(numero)

# EJERCICIO 12
# MOSTRAR LOS VALORES A,B,C,D,E
mensaje="A B C D"
for letra in mensaje:
    print(letra)


# EJERCICIO 13
# MOSTRAR "LOS ESTUDIANTES DE INGENERIA ELECTRONICA 2019"
mensaje="LOS ESTUDIANTES DE INGENERIA ELECTRONICA 2019"
for letra in mensaje:
    print(letra)

# EJERCICIO 14
# MOSTRAR EL ENUNCIADO
mensaje="MENOR SEA TU CANTIDAD MEJOR SERA TU CALIDAD"
for letra in mensaje:
    print(letra)

# EJERCICIO 15
# MOSTRAL LA LETRA "M" DEL ENUNCIADO
mensaje="MUCHAS GANAS DE COMPETIR CON LOS DEMAS"
contador=0
for letra in mensaje:
    if (letra=="M"):
        contador+=1

print("la letra M :",contador)
