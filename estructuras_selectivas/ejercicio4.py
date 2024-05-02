import random 
#se asgina un nuemro a azar
valor_de_compra= float(input("digite el valor de la compra:"))
#se asigna variable para el valor de la compra 
colores_balota=["rojo","azul","verde","negro"]
#se asigna variable para los colores de las balotas 
color_balota= random.choice(colores_balota)
if color_balota== "rojo":
    descuento= 0.20
    print("su descuento es del 15%")
elif color_balota=="azul":
 descuento= 0.00
 print("el descuento es de 0%")
elif color_balota=="verde":
   descuento=0.20
   print("el descuento es de 20%")
elif color_balota=="negro":
   descuento= 0.00
   print("el decuento es de 0%")

valor_a_pagar=(valor_de_compra*descuento)
descuento= (valor_de_compra-valor_a_pagar)

print("valor de compra:",valor_de_compra)
print("color de la balota:",color_balota)
print("valor a pagar:",descuento)