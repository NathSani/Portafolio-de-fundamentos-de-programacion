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
Años= 20
print (type(Años))
```
## Float

## String

## Casting en Python

## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
