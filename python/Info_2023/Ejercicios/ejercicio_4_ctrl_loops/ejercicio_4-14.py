## 14-Escribe un programa que pida al usuario un número y luego imprima un
## triángulo de números como el siguiente:
## 1
## 2 2
## 3 3 3
## 4 4 4 4
## 5 5 5 5 5

num_filas = int(input("ingrese un nro "))
cont = 1
for i in range(num_filas):
    print(cont * str(cont))
    cont += 1