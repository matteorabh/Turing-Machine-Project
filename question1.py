import outil

class MT(object):

    def __init__(self,etat,etat_bande,tete_lecture):
        self.etat = etat
        self.etat_bande = etat_bande
        self.tete_lecture = {}
        self.nb_bande = 0
        self.transitions = False

    def preparation_initial(self,fichier):
        with open(fichier) as f:
            lines = outil.supp_n(f.readlines())
        self.transitions = {lines[i] : lines[i+1] for i in range(0,len(lines),2)}
        self.nb_bande = lines[0].split(',')-1
        self.tete_lecture = {i:0 for i in range()}
        #Vérifications qu'il n'y a pas d'erreur dans le fichier
        outil.verif_determinisme(fichier,self.nb_bande,self.transitions)
        outil.verif_etat_initial_final(fichier)

    def affichage():
        print("--------------------------------")
        print()
        print("--------------------------------")

def initialisation(mot,fichier):
    M1 = MT('I',{1:mot},)
    M1.preparation_initial(fichier)
    return M1

M1 = initialisation('kayak','MT_Donnee.txt')
#M1.affichage()
    
