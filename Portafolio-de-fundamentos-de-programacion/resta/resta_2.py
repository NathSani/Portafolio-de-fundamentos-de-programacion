# Pedir al usuario un valor-. Si el valor es positivo 
# pedir un segundo valor y calcular la suma, resta y producto de ambos. Mostrar resultados por pantalla.

num= int (input("ingrese el numero: "))

if num>0:
    num2= int (input("ingrese el numero 2: "))
    print ("suma:", num+num2)
    print ("resta:", num-num2)
    print ("producto:", num*num2)

    print ("........")
