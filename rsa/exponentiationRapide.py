#!/usr/bin/python
#-*-coding:utf8-*-

def decToBin(i):
    """
        Retourne une chaine de caractère contenant i en binaire
    """
    result = ""

    while i != 0:
        result = str(i % 2) + result
        i = i / 2
    return result


def genereMot(e):
    """
        Retourne le mot (composé de S et X) correspondant à l'exposant e
    """
    bin = decToBin(e)
    result = bin[1:]
    word = ""

    for r in result:
        if r == "1":
            word += "SX"
        else:
            word += "S"

    return word


def puissanceRapide(x, e) :
    """
        Retourne un couple (x^e, liste des exposants calculés)
    """
    word = genereMot(e)
    result = x
    listExposants = [1]
    last = 1
    
    for l in word:
        if l == "S":
            result = result * result
            last = last * 2
        elif l == "X":
            result = result * x
            last = last + 1

        listExposants.append(last)

    return (result, listExposants)
    

def puissanceLente(x, e) :
    """
        Retourne le résultat de x^e 
    """
    result = 1

    for j in range(1, e + 1):
        result = result * x

    return result