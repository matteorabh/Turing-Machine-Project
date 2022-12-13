class MT(object):

    def __init__(self,etat,etat_bande,tete_lecture):
        self.etat = etat
        self.etat_bande = etat_bande
        self.tete_lecture = tete_lecture
        self.nb_bande = 0
        transitions = {}

    def preparation(fichier):
        with open("fichier.txt") as f:
            lines = supp_n(f.readlines())

        
            
        return

    def affichage():
        return

def initialisation(mot,fichier="MT_Donnee.txt"):
    M1 = MT()
    M1.preparation(fichier)
    return 
    
def supp_n(lines):
    """
    Fonction qui supprime les \n d'une liste
    (Utile après le stockage du fichier)
    """
    return [lines[i][:lines[i].find('\n')] for i in range(len(lines))]

