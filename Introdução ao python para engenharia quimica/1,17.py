""" Desenvolva um codigo que calcule o volume de um tanque de base hexagonal. Para que o calculo seja 
    realizado, seu codigo deve solicitar o valor do lado L do hexagano e a altura h ao usuario. O resultante
    do volume calculo deve ser impresso no console.
"""
import math

def volume_hexagono(l, h):
    return 6*(((l**2)*math.sqrt(3))/4)*h

l = float(input("Diga o valor do lado em metros: "))
h =float(input("Diga o valor da altura em metros: "))

print(f"O valor do volume é {volume_hexagono(l,h)}")