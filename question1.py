class MT(object):

    def __init__(self,etat,etat_bande,tete_lecture):
        self.etat = etat
        self.etat_bande = etat_bande
        self.tete_lecture = tete_lecture

def initialisation(mot,fichier="MT_Donnee.txt"):
    l_mot = [lettre for lettre in mot]
    return MT('I',l_mot,0)


# Doit-on faire des unittest ?
# Question 2 : machine de turing = fichier ou = class MT
