# Ejercicio 01
msg="FORMATO"
print(msg.rjust(20))
print("#" * 20)

# Ejercicio 02
nro="0.23"
print(nro.zfill(8))

# Ejercicio 03
nro="25"
print(nro.zfill(15))

# Ejercicio 04
nro="321"
print(nro.zfill(6))

# Ejercicio 05
msg="SANDOVAL"
print(msg.center(30))
print("#"*30)

# Ejercicio 06
msg="valor del {billete}"
print(msg.format(billete="10 soles"))

# Ejercicio 07
msg="Hello {} tu promedio finales es {}"
print(msg.format("Yoel","14"))

# Ejercicio 08
msg="El lunes {} presenataran su {} final"
print(msg.format("25","proyecto"))

# Ejercicio 09
mensaje="El valor del dolar es {dolar} en soles"
print(mensaje.format(dolar="3.12"))

# Ejercicio 10
mensaje="El numero de PI equivale a {nro}"
print(mensaje.format(nro="3.14"))

# Ejercicio 11
producto="Caña"
precio=1.54
mensaje="El producto {prod} cuesta {prec}"
print(mensaje.format(prod=producto, prec=precio))

# Ejercicio 12
consumo="Leche"
precio=1.8
mensaje="Elmer por la mañanas compra {consumo} ,cuesta {precio}"
print(mensaje.format(consumo=consumo,precio=precio))

# Ejercicio 13
mensaje="La facultad de {} ha organizado un viaje a la {}"
print(mensaje.format("FACFYM","CAJAMARCA"))

# Ejercicio 14
mensaje="los ingresantes de ciclo academico 2019-II es de {:d} estudiantes"
print(mensaje.format(41))

# Ejercicio 15
msg="CONCLUIDO EL FORMATO"
print(msg.center(50))
print("#"*50)
