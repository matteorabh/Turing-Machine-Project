from outil import supp_n, verif_etat_initial_final


class MT(object):

    def __init__(self,etat):
        self.etat = etat
        self.etat_bande = {}
        self.tete_lecture = {}
        self.nb_bande = 0
        self.transitions = False

    def preparation_initial(self,fichier,mot):
        with open(fichier) as f:
            lines = supp_n(f.readlines())

        self.transitions = {lines[i] : lines[i+1] for i in range(0,len(lines),2)}
        self.nb_bande = len(lines[0].split(','))-1
        self.tete_lecture = {i:0 for i in range(1,self.nb_bande+1)}
        self.etat_bande = {i :['_'] for i in range(1,self.nb_bande+1)}
        self.etat_bande[1] = [lettre for lettre in str(mot)]

        #Vérifications qu'il n'y a pas d'erreur dans le fichier
        #outil.verif_determinisme(fichier,self.nb_bande,self.transitions)
        verif_etat_initial_final(fichier)

    def element(self):
        print('état courant :', self.etat)
        print('nombre de bande :', self.nb_bande)
        print('état des bandes :', self.etat_bande)
        print('position tete de lecture pour chaque bande :', self.tete_lecture)
        print('Les transitions du fichier :', self.transitions)

    def affichage():
        print("--------------------------------")
        print()
        print("--------------------------------")

def initialisation(mot,fichier):
    M1 = MT('I')
    M1.preparation_initial(fichier,mot)
    return M1

M1 = initialisation('1010','MT_Donnee.txt')
M1.element()
    
