nota1 = float(input("digite la primera nota:"))
#asignar una variable para digitar la cantidad de la primera nota
nota2 = float(input("digite la segunda nota:"))
#asignar una variable para digitar la cantidad de la segunda nota
nota3 = float(input("digite la tercera nota:"))
#asignar una variable para digitar la cantidad de la tercera nota
promedio= (nota1 + nota2 + nota3)/3
#se asigna variable para calcular el promedio de las notas 
if promedio >=70:
    print ("el estudiante aprueba", promedio)
else:
    print("el estudiante reprueba",promedio)
    #se usa print para imprir los resultados 