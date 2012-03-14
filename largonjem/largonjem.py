#-*-coding:utf8-*-

import sys

class Largonjem :

    """
        Crypte un mot en Largonjem
    """
    @staticmethod
    def wordLargonjem(word):
        
        if word[0] not in "aeiouyAEIOUY":
            result = "l"
            lword = len(word)
            for i in range(1, lword):
                result += word[i]

            result += word[0] + "em"
        else:
            result = word

        return result


    """
        Crypte un texte en Largonjem
    """
    @staticmethod
    def textLargonjem(text):
        
        words = text.split(" ")
        result = ""

        for word in words:
            result += wordLargonjem(word) + " "

        return result


if __name__ == "__main__":
    text = raw_input("Texte à crypter : ")
    print Largonjem.textLargonjem(text)
    sys.exit(0)
