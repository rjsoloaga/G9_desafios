## 1-Escribe un programa que pida al usuario una palabra y luego imprima cada
## letra de la palabra en una línea separada.

palabra = input("Ingrese una palabra ")

cont = palabra.__len__()
for i in palabra:
    if cont > 0:
        print(i)
    else:
        break
