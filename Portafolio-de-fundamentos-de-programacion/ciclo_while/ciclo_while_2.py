#Ingresar numeros enteros, repetir el ciclo hasta que el usuario ingrse el numero: 0
#Contar los numeros ingresados
num=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        num+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", num)