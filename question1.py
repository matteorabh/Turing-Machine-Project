class MT (object):

    def __init__(self,etat,etat_bande,tete_lecture,fichier):
        self.etat = etat
        self.etat_bande = etat_bande
        self.tete_lecture = tete_lecture
        self.fichier = fichier


def initialisation(mot=input("Veuillez sélectionner un mot d'entrée"),fichier="MT_Donnee.txt"):
    return MT('I',mot,0,fichier)


# Doit-on faire des unittest ?
