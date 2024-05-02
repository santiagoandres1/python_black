cantidad_total_de_compra=float(input("digite la cantidad total de la compra:"))
#se asgina variable para digitar el valor total de la compra
if  cantidad_total_de_compra <500000:
      #se utiliza if para indicar que si el monto total es mayor que 500000 entotes hacer:
      dinero_propio= cantidad_total_de_compra *0.55
      #se asigna varibale para digitar cantidad de porcentaje del dinero propio
      prestamo_banco= cantidad_total_de_compra *0.30
      # se asigna varibale para digitar cantidad de porcentaje del prestamo del banco
      credito_fab= (cantidad_total_de_compra * 0.15)
       #se asigna varibale para digitar cantidad de porcentaje del credito del fabricante
      intereses_compra= (credito_fab)+(credito_fab *0.20) 
      #se asigna variable para los intereses y se realiza operacion para saber la cantidad de dinero
      
else :
      dinero_propio= (cantidad_total_de_compra *0.70)
       #se asigna varibale para digitar cantidad de porcentaje del dinero propio
      credito_fab= (cantidad_total_de_compra *0.30)
      #se asigna varibale para digitar cantidad de porcentaje del credito del fabricante
      intereses_fab= (credito_fab)(credito_fab *0.20)
      #se asigna varibale para digitar cantidad de porcentaje del credito del fabricante
      prestamo_banco= 0
      
print ("digite cantidad de dinero propio invertido:", dinero_propio)
print ("digite cantidad de dinero prestado del banco:",prestamo_banco)
print ("digite cantidad de dinero solicitado al fabricante:",credito_fab)       
#se utiliza print para imprimir los resultados 