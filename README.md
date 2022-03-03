# Portafolio "fundamentos de programación " #

# Qué es Python?
Es un lenguaje de programacion de alto nivel, utlizado por grandes desarrolladores por su gran capacidad para crear programas de todo tipo. Este lenguaje a diferencia de otro es de tipo interprete quiere decir que no se necesita compilar para ejecutar los programas realizados. Su gran ventaja es que se ejecuta desde el ordenador y no necesita ser traducido a lenguaje de máquina. 

# Qué es una variable?
Una variable en programación es un espacio en donde se almacenera información, esta se caracteriza por ser inestable, inconstante y mudable.  en Python las variables son consideradas como "Etiquetas" y hacen referencia a los datos almacenados en dicha variable.

``` python 
b = 8
```

## Nombrando una variable
Podemos asignar nombres a nuestras variables, siempre y cuando no usemos palabras reservadas de Python. Esto debido a que si nosotros usamos una función ya no sería variable si no cumpliría con otro objetivo, para nombrar variables correctamente debemos tener en cuenta los espacios o guiones.

**Manera correcta de asignar:**
``` python 
compu = 10 
_Compu = 12
com_pu = 13
cOMpu = 14

``` 
**Manera incorrecta de asignar:**
``` python 
tra-duccion= 10
tra duccir= 10
.traducir= 10
``` 

## Asignando valores a una variable

Las variables pueden contener un número, una cadena o un valor lógico (verdadero/falso). Para eso usaremos el operador de asignacion el cual es: (=) asi de le dara un valor a la variable y esta se mantendrá hasta que el programa termine de ejecutarse o hasta que se le asigne un nuevo valor.

 ``` python 
# Asigna a la variable <b> el resultado de la expresion 2+2
b = 2 + 2 
```

## Operadores básicos

Los operadores basicos son:  ( suma, resta, multiplicacion, división y módulo), dichas operaciones son usadas para realizar operaciones matemáticas. Son esenciales aprenderlas porque serán el principio de cosas más complicadas. **Simbolos: (+), (-), (*) (/), (%)** .

### Suma
La suma es una operación aritmética que consiste en reunir varias cantidades en una sola, su simbolo representativo en python es **(+)**.

``` python 
a = 4
b = 8
sum= a+b 
print(a,'+',b,'=',sum)
```
**Salida:**
``` python 
12
```
### Resta
La resta es una operación aritmética que consiste en quitar una cantidad (el sustraendo) de otra (el minuendo) para averiguar la diferencia entre las dos. Su representación en Python se da por medio del operador **(-)**.
``` python 
a = 10
b = 2 
rest= a-b
print(a,'-',b,'=',rest)
```
**Salida:**
``` python 
8
```
### Multiplicación

La multiplicación se utiliza para encontrar el producto de 2 valores. En Python es representada por el operador asterisco **(*)**. EL cual es "el operador de multiplicación".

``` python 
Num1 = 2
Num2 = 5
mult = Num1*Num2
print(Num1,'*',Num2,'=',mult)
```
**Salida**
``` python 
10
```
### División
Para la realizar el cociente entre dos números en Python debemos utilizar el operador **(/)**, La división es la operación contraria a la multiplicación. Para saber si la división es correcta se debe multiplicar el resultado, también llamado cociente, por el divisor.
``` python 
num1 = 8
num2 = 4
div= num1/num2
print(num1,'/',num2,'=',div)
```
**Salida**
``` python 
2
```

### Módulo
Para calcular el módulo en Python utilizamos el operador **(%)**, esta operación la utilizamos para encontrar el **resto** "cuando el primer operando se divide por el segundo".

``` python 
num1 = 5
num2 = 2
mod= num1%num2
print(num1,'%',num2,'=',mod)
```
**Salida:**
``` python 
1
```
# Tipos de datos en Python

Los tipos de datos definen un conjunto de valores que tienen una serie de características y propiedades determinadas. Los tipos de datos básicos de Python son los booleanos, los numéricos **(enteros, punto flotante y complejos)** y las cadenas de caracteres.

// :D //

## Integer
Integer es un tipo de dato en donde solo pertenecen lo enteros, estos constan de una serie sin comillas de sólo dígitos; es decir, no contienen comas decimales ni exponentes. En Python el conjunto está limitado realmente por la capacidad de la memoria disponible, no hay un límite de representación impuesto por el lenguaje.

**Ejemplo:**
``` python 
Años = 20
print (type(Años))
```
## Float
El tipo de dato numérico **float** permite representar un número positivo o negativo con decimales, es decir, números reales. Los valores float son almacenados de una forma muy particular, denominada representación en coma flotante.

**Ejemplo:**
``` python 
A = 0.152024
print (A)
print (type(A))
```
## String
Las cadenas en Python o tambien conocidas como  **strings** son un tipo inmutable que permite almacenar secuencias de caracteres. Para utilizar String en Python se debe utlizar **(" ")** o tambien podemos usar comillas simples **(' ')**.

**Ejemplo con comillas:**
``` python 
a = "Hola esto es un código"
print (a)
print (type(a))
```

**Ejemplo con comilla simple:**
``` python 
a = 'Hola esto es un código'
print (a)
print (type(a))
```

## Casting en Python
En python casting es utilizado para convertir un tipo de dato a otro. Esto quiere decir que nosotros podemos cambiar el dato original a otro tipo de dato, existen 2 tipos de casting y son: 

Casting implícito:Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.

Casting explícito:Es tipo de casting es realizado por nosotros, tenemos la potestad de cambiar nuestro dato al que queremos.

**Ejemplo de casting implícito:**
``` python
a = 8
b = 12.5
res = a+b
print (type(res))
```
**Ejemplo de casting explícito:**
``` python
a =3.24
a = int(a)
print (a)
```
## List
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Las propiedades de la listas son: 

**Ordenadas, Pueden ser formadas por tipos arbitrarios, posibilidad de indexar, pueden anidarse unas a otras, son mutables y dinámicas.**
``` python 
list = [1, 2, 3, 4, 5, 6, 7, 8]
lista = [10, "Hola mundo", 15.25, [1, 2, 3, 4, 7, 8]]
```
## Tuple
Tuple o tupla en Python son un tipo de estructura similar a una lista, pero con una gran diferencia el cual es de tipo inmutable quiere decir que al ser declaradas ya no se pueden modificar. La tupla al igual que la lista permite almacenar datos. 
``` python 
tup= 10, 20, 30
print (tup) 
```
``` python 
c = (8, 9, 10)
x, y, z = c
print(x, y, z)
``` 
## Dictionary
Los diccionarios son una estructura de datos que nos permite almacenar su contenido en forma de llave y valor. En Python son considerados como colección de elementos. se crea de la siguiente manera para inicar cada uno contiene una **({})**, seguido con la separación de una **(,)**.
``` python 
n1= {
  "Nombre": "Juan",
  "Edad": 10, 
  "Documento": 2565478
}
print(n1)
```
# Tomando decisiones
En esta parte de la programación entraremos al mundo de los ciclos y sentencias.
**if**, **for**, **break**, **continue**, **while**.

## Sentencia if
La sentencia de condición IF nos permitira tomar decisiones, en un lenguaje de programación es muy importante ya que no permitira cambiar el flujo del programa. If al español Si, nos permitita que los bloques de código se ejecuten si y solo si se dan unas condiciones particulares.
Su sintaxis es de la siguiente manera: 
**IF: (condición)**

**(true): Se ejecuta el bloque de sentencias.**

**(false):Ne ejecuta el bloque de sentencias.**
``` python 
a = 8
b = 9
if b! = 0 
   print (a/b)
```
``` python 
a = 10
if a > 6 and a < 13:
    print("Mayor que 6 y menor que 13")
``` 

## If - Else
La sentencia IF-Else es utilizada para evaluar 2 condiciones ya sea si esta se cumple se ejecutara, lo mismo pasara si no se cumple se emite un mensaje. If al español SI, Else al español Si no, para expresear dicha condición se realiza de la siguiente manera:

**(true): Se ejecuta el bloque de sentencias.**

**(false): Se ejecuta el bloque de sentencias solo cuando la condición tiene como resultado falso.**

``` python 
num1= 23
num2= 11

if num1 > num2:
    print ('El mayor es', num1)
    if num1%2 == 0:
        print ("Y es un numero par")

    else:
        print ("y es un numero impar")
 
else: 
    print ('El mayor es', num2)
    print ('El menor es', num1)
 ``` 
## Ciclo For
El bucle for tiene un parecido con el ciclo While pero no son iguales. La principal diferencia con respecto al while esta en la condición. En el while la condición sera evaluada en cada iteración y esta se deice si vuelve a ejecutar o no el código, con respecto for no existe dicha  condición, sino un **iterable** que define las veces que se ejecutará el código. 

``` python 
n=7
suma=0
for i in range (n):
    nota= float(input('Ingrese nota:'+ str (i+1)+ ':' ))
    suma += nota

promedio = suma/n
print ('Promedio', promedio)
```
## Ciclo While
El bucle while nos permitira ejecutar nuestro código repetidas veces, por eso se le llama como ciclo repetitivo. El código se ejecutará unicamente si la condición determinada se cumple. Cuando esta deje de cumplirse, automaticamente se saldrá del bucle y se continuará la ejecución normal. 

``` python 
num= 11
while num < 10 or num > 20 or num%2 !=0:
    num = int (input('Ingrese numeros positivos: '))
```
## Break
Break es una sentencia el cual va alterar el funcionamiento de los ciclos ya sean como While o for. Practicamente una vez se encuentra la palabra break, el bucle se habrá terminado.
``` python 
contador= 0
for i in range (10):
    for j in range (10):
        contador+= 1
        print ('i: ', i, 'j: ', j)
        if contador > 50:
            break
print ('contador', contador )
```
## Continue
La sentencia continue tambien nos permite modificar el compartamiento de los ciclos. Pero con una gran diferencia en **Continue** se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar. No rompera el ciclo solo saltara el código pendiente.
``` python 
cad = 'Python'
for let in cad:
    if let == 'P':
        continue
    print(let)
 ```
 #Gracias    

