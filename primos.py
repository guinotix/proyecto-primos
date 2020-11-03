from random import randint
from typing import *

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

def suma_primos(lista: List[int]) -> int:
    suma = 0
    for num in lista:
        suma += num
    return suma


if __name__ == '__main__':

    cantidad = int(input("Cuantos numeros van a la lista?: "))
    lista_numeros = []
    while cantidad > 0:
        un_numero = randint(1, 10)
        lista_numeros.append(un_numero)
        cantidad -= 1

    print(lista_numeros)

    for numero in lista_numeros:
        if es_primo(numero):
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")

    # Mostrar la suma de los numeros primos en la lista
    print(f"La suma de los primos es: {suma_primos(lista_numeros)}")