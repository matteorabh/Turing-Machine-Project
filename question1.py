import outil

class MT(object):

    def __init__(self,etat,etat_bande,tete_lecture):
        self.etat = etat
        self.etat_bande = etat_bande
        self.tete_lecture = tete_lecture
        self.nb_bande = 0
        self.transitions = False

    def preparation(self,fichier):
        with open(fichier) as f:
            lines = outil.supp_n(f.readlines())
        self.transitions = {lines[i] : lines[i+1] for i in range(0,len(lines),2)}
        self.nb_bande = lines[0].split(',')-1

    def affichage():
        return

def initialisation(mot,fichier):
    M1 = MT('I',,0)
    M1.preparation(fichier)

initialisation('kayak','MT_Donnee.txt')
    
