#!/usr/bin/python
#-*-coding:utf8-*-


"""
    Retourne une chaine de caractère contenant i en binaire
"""
def decToBin(i):
    result = ""

    while i != 0:
        result = str(i % 2) + result
        i = i / 2
    return result


"""
    Retourne le mot (composé de S et X) correspondant à l'exposant e
"""
def word_generate(e):
    bin = decToBin(e)
    result = bin[1:]
    word = ""

    for r in result:
        if r == "1":
            word += "SX"
        else:
            word += "S"

    return word


"""
    Retourne un couple (x^e, liste des exposants calculés)
"""
def puissanceRapide(x, e) :
    word = word_generate(e)
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
   

"""
    Retourne le résultat de x^e 
"""
def puissanceLente(x, e) :
    result = 1

    for j in range(1, e + 1):
        result = result * x

    return result