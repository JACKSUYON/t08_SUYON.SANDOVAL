#operacion formato nro 1
cad="BOLETA DE PAGO"
print("#" * 28)
print(cad.center(28))
print("#" * 28)

#operacion formato nro 2
nro_clientes="123"
print(nro_clientes.zfill(5))

#operacion formato nro 3
mensaje="CAMINANTES SON TUS HUELLAS {0:10}"
print(mensaje.format("EL CAMINO Y NADA MAS"))

#operacion formato nro 4
frase="DICHOSO EL ARBOL {0:>100}"
print(frase.format("QUE ES APENAS SENSITIVO"))

#operacion formato nro 5
msg="{0:d} estudiantes con calificacion {1:.2f}"
print(msg.format(28,14.4980))

#operacion formato nro 6
msg="hay {:d} cachimbos de ka escuela de ingenieria electronica"
print(msg.format(45))

#operacion formato nro 7
gravedad=9.85234313
mensaje="el valor de la gravedad es {:.4f}"
print(mensaje.format(gravedad))

#operacion formato nro 8
msg="Hola amigo {} tu promedio final es {}"
print(msg.format("Frank",15))

#operacion formato nro 9
mensaje="Pago por la compra de {Producto}"
item="Laptop"
print(mensaje.format(Producto=item))

#operacion formato nro 10
producto="Atun"
precio=3.1
mensaje="El producto {produ} cuesta S/. {prec}"
print(mensaje.format(produ=producto, prec=precio))

#operacion formato nro 11
servicio="Lus"
Pago=45.23
mensaje="El pago po el servicio de {0} es S/.{1}"
print(mensaje.format(servicio,Pago ))

#operacion formato nro 12
restaurante="EL NORTEÑITO"
print("el mejor restaurante de la region lambayeque es "+ restaurante.rjust(58) )
#operacion formato nro 13
monto="23.4"
print(monto.zfill(6))

#operacion formato nro 14
msg="hola {1} el precio es {0}"
print(msg.format(23,"Victor"))

#operacion formato nro 15
msg="FIN DE OPERACION FORMATO"
print("#" * 40)
print(msg.center(40))
print("#" * 40)
