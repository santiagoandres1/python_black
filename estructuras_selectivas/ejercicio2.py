comprasdelaszapatillas = float(input("ingrese el valor de la compra"))
#se asigna variable para digitar el valor de la compra 
cantidad =int(input("ingrese la cantidad de zapatos que lleva:"))
#se asigna varibale para para digitar el valor de la cantidad de zapatos pata llevar 
oferta_descuento1= comprasdelaszapatillas * (1 -0.1)
oferta_descuento2= comprasdelaszapatillas * (1 -0.2)
#se asigna una variable para realizar la operacion de descuentos 
if cantidad >=3:
    valor= comprasdelaszapatillas - oferta_descuento2
    print("se aplico un descuento del 20(%)", valor)
else:
    valor= comprasdelaszapatillas - oferta_descuento1
    print("se aplica un descuento del 10(%)", valor)
    #se usa print para imprimir los resultados 