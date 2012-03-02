#!/usr/bin/python
#-*-coding:utf8-*-

import random
from math import *
from exponentiationRapide import *


"""
    Retourne le PGCD de a et b
"""
def pgcd(a, b):
    if a % b == 0:
        return b

    return pgcd(b, a % b)


"""
    Retourne le nombre de facteurs de n   
"""
def nombreFacteur(n):
    count = 2
    r = sqrt(n)
    i = 2
    
    while i <= r:
        if n % i == 0:
            count = count + 1
        i = i + 1
    
    return count


"""
    Retourne un boolean (n est premier ou non) 
"""
def estPremier(n):
    return nombreFacteur(n) == 2

"""
    Retourne le résultat de x^k
"""
def puissance(x, k):
    return puissanceRapide(x, k)[0]


"""
    Retourne la liste des nombres premiers inférieurs à n
"""
def listNombrePremierInf(n):
    return [i for i in range(1, n) if estPremier(i)]


"""
    Retourne un nombre premier aléatoire entre 500 et 2000
"""
def nombrePremier():
    trouve = False

    while not trouve:
        n = random.randint(500, 2000)
        
        if estPremier(n):
            trouve = True

    return n