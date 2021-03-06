#!/usr/bin/python
#-*-coding:utf8-*-

import random
import sys
from fonctions import *


class Rsa :
    
    """
        Génère la clé public et la clé privée
    """
    @staticmethod
    def genereCles(P, Q):
        """ GENERE CLE PUBLIC """
        n = P * Q
        phiden = (P - 1) * (Q - 1)

        e = max(P, Q)
        
        trouve = False

        while not trouve and e < phiden:
            e = e + 1
            
            if pgcd(e, phiden) == 1 :
                trouve = True 
        
        if e == phiden:
            print "Erreur ! (e = phiden)" 
            sys.exit(0)
        
        """ GENERE CLE PRIVEE """
        f = max(P, Q)
        
        trouve = False
        
        while not trouve and f < phiden:
            f = f + 1
            
            if (e * f) % phiden == 1:
                trouve = True   
        
        """ Retourne un couple (module de chiffrement, clé publique), (module de chiffrement, clé privee) """
        return ((n, e), (n, f))


    """
        Crypte l avec la clé publique
    """
    @staticmethod
    def crypter(l, clePub):
        (n, c) = clePub
        
        return puissance(l, c) % n


    """
        Crypte le message clair avec la clé publique
    """
    @staticmethod
    def crypterMessage(msgClair, clePub):
        return "-".join([str(Rsa.crypter(ord(l), clePub)) for l in msgClair])
    

    """
        Décrypte l avec la clé privée
    """
    @staticmethod
    def decrypter(l, clePrivee):
        
        (n, d) = clePrivee
        return puissance(l, d) % n


    """
        Décrypte le message chiffré avec la clé privée
    """
    @staticmethod
    def decrypterMessage(msgChiffre, clePrivee):
        return "".join([chr(Rsa.decrypter(int(l), clePrivee)) for l in msgChiffre.split("-")])


if __name__ == '__main__':
    print
    print "====== NOMBRES PREMIERS P ET Q ======="
    p = nombrePremier()
    q = nombrePremier()
    while q == p:
        q = nombrePremier()
    print "P = ", p
    print "Q = ", q
    print

    print "======= GENERATION DES CLEES PUBLIQUE ET PRIVEE ======="
    (clePub, clePrivee) = Rsa.genereCles(p, q)
    print "Clé publique : ", clePub
    print "Clé privée : ", clePrivee
    print

    print "======= MESSAGE A CRYPTER ======="
    msgClair = "Ecole"
    print "Message à crypter :", msgClair
    print

    print "======= MESSAGE CRYPTE ======="
    msgChiffre = Rsa.crypterMessage(msgClair, clePub)
    print "Message crypté : ", msgChiffre
    print

    print "======= MESSAGE DECRYPTE ======="
    msgDechiffre = Rsa.decrypterMessage(msgChiffre, clePrivee)
    print "Message décrypté :", msgDechiffre
    print

    print "======= FIN ======="
    sys.exit(0)