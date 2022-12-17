from outil import supp_n, verif_etat_initial_final, verif_determinisme, verif_decalage, verif_alphabet
import time


class coloration:
    ROUGE = '\033[91m' 
    RESET = '\033[0m' 


class MT(object):

    def __init__(self,etat):
        self.etat = etat
        self.etat_bande = {}
        self.tete_lecture = {}
        self.nb_bande = 0
        self.transitions = False

    def preparation_initial(self,fichier,mot):
        """
        Instancie les variables d'instance à partir 
        du fichier contenant le code de la Machine de Turing.
        """
        with open(fichier) as f:
            lines = supp_n(f.readlines())

        self.transitions = {lines[i] : lines[i+1] for i in range(0,len(lines),2)}
        self.nb_bande = len(lines[0].split(','))-1
        self.tete_lecture = {i:0 for i in range(1,self.nb_bande+1)}
        self.etat_bande = {i :['_'] for i in range(1,self.nb_bande+1)}
        self.etat_bande[1] = [lettre for lettre in str(mot)]

        #Vérifications qu'il n'y a pas d'erreur dans le fichier
        verif_determinisme(fichier)
        verif_etat_initial_final(fichier)
        verif_decalage(fichier,self.nb_bande)
        verif_alphabet(fichier,self.nb_bande)

    def element(self):
        """
        Fais apparaître chaque variable d'instance d'une Machine de Turing.
        Utile pour les tests.
        """
        print('état courant :', self.etat)
        print('nombre de bande :', self.nb_bande)
        print('état des bandes :', self.etat_bande)
        print('position tete de lecture pour chaque bande :', self.tete_lecture)
        print('Les transitions du fichier :', self.transitions)

    def affichage(self):
        """
        Affiche explicitement la configuration de la Machine de Turing à un instant T.
        Chaque bande est affiché. Et en rouge est indiqué où se situe la tête de lecture
        """
        print("--------------------------------")
        for i in range(1,self.nb_bande+1):
            liste = self.etat_bande[i]
            mot = ''
            for j in range(len(liste)):
                if j != self.tete_lecture[i]:
                    mot += liste[j] + ' '
                else:
                    mot = mot + coloration.ROUGE + liste[j] + coloration.RESET + ' '
            print(mot)
        print("--------------------------------")
        time.sleep(0.5)


def initialisation(mot,fichier):
    """
    Permet d'initialiser une machine de Turing à partir d'un mot et d'un fichier.
    """
    M1 = MT('I')
    M1.preparation_initial(fichier,mot)
    return M1

    
