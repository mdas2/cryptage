#!/usr/bin/python
#-*-coding:utf8-*-

import random
from math import *
from exponentiationRapide import *


def pgcd(a, b):
    """
        Retourne le PGCD de a et b
    """
    if a % b == 0:
        return b

    return pgcd(b, a % b)


def nombreFacteur(n):
    """
        Retourne le nombre de facteurs de n   
    """
    count = 2
    r = sqrt(n)
    i = 2
    
    while i <= r:
        if n % i == 0:
            count = count + 1
        i = i + 1
    
    return count


def estPremier(n):
    """
        Retourne un boolean (n est premier ou non) 
    """
    return nombreFacteur(n) == 2


def puissance(x, k):
    """
        Retourne le résultat de x^k
    """
    return puissanceRapide(x, k)[0]


def differenceList(a, b):
    """
    Renvoie la différence de 2 listes
    """
    R = []
    for i in a :
        if i not in b :
            R.append(i)
    for i in b :
        if i not in a :
            R.append(i)
    return R


def listNombrePremierInf(n):
    """
        Retourne la liste des nombres premiers inférieurs à n
    """
    return [i for i in range(1, n) if estPremier(i)]


def nombrePremier():
    """
        Retourne un nombre premier aléatoire entre 500 et 2000
    """
    trouve = False

    while not trouve:
        n = random.randint(500, 2000)
        
        if estPremier(n):
            trouve = True

    return n