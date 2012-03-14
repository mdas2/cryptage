#!/usr/bin/python
#-*-coding:utf8-*-

from fonctions import *

class ElGamal:

    """
        Génère clé publique et clé privée
    """
    @staticmethod
    def keys(p, g, a):
        A = g ** a % p
        public = (p, g, A)
        private = a
        return (public, private)


    """
        Crypte un nombre avec la clé publique et b
    """
    @staticmethod
    def encrypt(message, public, b):
        (p, g, A) = public
        B = g ** b % p
        c = message * A ** b % p
        return (B, c)


    """
        Decrypte un nombre avec la clé publique et la clé privée
    """
    @staticmethod
    def decrypt(cryptogram, public, private):
        (p, g, A), a = public, private
        (B, c) = cryptogram
        msg = B ** (p - 1 - a) * c % p
        return msg


    """
        Crypte un message avec la clé publique et b
    """
    @staticmethod
    def encryptText(text, public, b):
        encryptText = []
        for l in text:
            (B, c) = ElGamal.encrypt(ord(l), public, b)
            encryptText.append(c)
        return (B, encryptText)   


    """
        Décrypte un message avec la clé publique et la clé privée
    """
    @staticmethod
    def decryptText(cryptogram, public, private):
        (B, encryptText) = cryptogram
        decryptText = ""
        for lc in encryptText:
            decryptText += chr(ElGamal.decrypt((B, lc), public, private))
        return decryptText


if __name__ == '__main__':

    print
    p = nombrePremier()
    g = racinePrimitive(p)
    print "p = ", p
    print "g = ", g
    ep = p - 2;

    print
    print "########## TITI ##########"
    print "Choisis un nombre entre 0 et", ep
    a = input()
    (publicKey, privateKey) = ElGamal.keys(p, g, a)
    print "Clé publique :", publicKey
    print

    print "########## TOTO ##########"
    print "TOTO récupère la clé publique de TITI ..."  
    print "TOTO choisis un nombre entre 0 et", ep  
    b = input()
    print "TOTO crypte son message et l'envoie à TITI"
    
    print
    msg = "Le chat est dans l'arbre."
    encryptText = ElGamal.encryptText(msg, publicKey, b)
    print "Message : ", msg
    print "Message crypté : ", encryptText
    
    print
    print "########## TITI ##########"
    print "TITI décrypte le message"
    decryptText = ElGamal.decryptText(encryptText, publicKey, privateKey)
    print "Message décrypté : ", decryptText
    print