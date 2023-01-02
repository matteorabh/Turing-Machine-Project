from outil import supp_n, verif_etat_initial_final, verif_determinisme, verif_decalage, verif_alphabet
import time


#######################################################
# Question 1

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
        Chaque bande est affiché. Et en rouge est indiqué où se situe la tête de lecture.
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

    
#######################################################
# Question 2

def allonge_bande(liste,binaire):
    """
    Permet d'aggrandir la bande. 
    Ajoute un _ à la fin de la liste si la tête de lecture avance. 
    Ajoute un _ au début de la liste si la tête de lecture recule. 
    """
    if binaire == 0:
        l = ['_'] 
        l.extend(liste)
        return l if liste[0] != '_' else liste
    else:
        return liste.append('_') if liste[-1] != '_' else liste

def pas(MT):  
    """
    Effectue un pas de calcul de la Machine de Turing. 
    """
    if MT.transitions != False:
        nb_bande = MT.nb_bande
        ligne_1 = MT.etat

        #recupération données
        for i in range(1,nb_bande+1):
            ligne_1 += ',' + MT.etat_bande[i][MT.tete_lecture[i]]
        try:
            ligne_2 = MT.transitions[ligne_1].split(',')
        except:
            print('Erreur de transitions! Le code est mal construit.')
            exit()

        #modification
        MT.etat = ligne_2[0]
        for i in range(1,nb_bande+1):
            MT.etat_bande[i][MT.tete_lecture[i]] = ligne_2[i]
            if ligne_2[i+nb_bande] == '>':
                MT.tete_lecture[i] += 1
                allonge_bande(MT.etat_bande[i],1)
            elif ligne_2[i+nb_bande] == '<':
                MT.etat_bande[i] = allonge_bande(MT.etat_bande[i],0)

    else:
        print("Vous n'avez pas initialisé votre machine de Turing!")
        exit()


#######################################################
# Question 3

def simulation(mot,MT):
    """
    Simule l'avancée d'une machine de Turing jusqu'à ce que l'état final soit trouvé 
    ou lorsque l'état cherché n'existe pas. 
    """
    MT.etat_bande[1] = [lettre for lettre in mot]
    while MT.etat != 'F':
        pas(MT)
    print()
    print('La simulation de la machine de Turing est terminé !')
    print()


#######################################################
# Question 4

def simulation_precise(mot,MT):
    """
    Simule l'avancée d'une machine de Turing jusqu'à ce que l'état final soit trouvé 
    ou lorsque l'état cherché n'existe pas. 
    Décris chaque étape dans le terminal.
    """
    MT.etat_bande[1] = [lettre for lettre in mot]
    MT.affichage()
    while MT.etat != 'F':
        pas(MT)
        MT.affichage()
    print()
    print('La simulation de la machine de Turing est terminé !')
    print()

#######################################################
# Question 6

def assemble_machines(mot, MT1) :
    with open("MT3.txt", "w") as MT3 :
        trans11 = list(MT1.transitions.keys())
        trans12 = list(MT1.transitions.values())
        for i in range(len(MT1.transitions)) :
            if len(trans11[i].split(',')) == MT1.nb_bande + 3 :
                MT2_initial = trans11[i].split(',')[0]
                MT2_nom = trans11[i].split(',')[MT1.nb_bande +1]
                MT2_final = trans11[i].split(',')[MT1.nb_bande+2]
                continue
            MT3.write(str(trans11[i]) + '\n')
            MT3.write(str(trans12[i]) + '\n')
        MT2 = initialisation(mot, MT2_nom.replace('"', ''))
        trans21 = list(MT2.transitions.keys())
        trans22 = list(MT2.transitions.values())
        for index in range(len(MT2.transitions)) :
            if list(trans21[index][0])[0] == 'I' :
                MT3.write(MT2_initial + "," + str(trans21[index].split(',')[1]) + "," + str(trans21[index].split(',')[2]) + "," + str(trans21[index].split(',')[3]) + '\n')
                MT3.write(str(trans22[index].split(',')[0]) + "MT2," + str(trans22[index].split(',')[1]) + "," + str(trans22[index].split(',')[2]) + "," + str(trans22[index].split(',')[3]) + "," + str(trans22[index].split(',')[4]) + "," + str(trans22[index].split(',')[5]) + "," + str(trans22[index].split(',')[6]) + '\n')
                continue
            if trans22[index][0] == 'I' :
                MT3.write(str(trans21[index].split(',')[0]) + "MT2," + str(trans21[index].split(',')[1]) + "," + str(trans21[index].split(',')[2]) + "," + str(trans21[index].split(',')[3]) + '\n')
                MT3.write(MT2_initial + "," + str(trans22[index].split(',')[1]) + "," + str(trans22[index].split(',')[2]) + "," + str(trans22[index].split(',')[3]) + "," + str(trans22[index].split(',')[4]) + "," + str(trans22[index].split(',')[5]) + "," + str(trans22[index].split(',')[6]) + '\n')
                continue
            if trans22[index][0] == 'F' :
                MT3.write(str(trans21[index].split(',')[0]) + "MT2," + str(trans21[index].split(',')[1]) + "," + str(trans21[index].split(',')[2]) + "," + str(trans21[index].split(',')[3]) + '\n')
                MT3.write(MT2_final + "," + trans22[index].split(',')[1] + "," + trans22[index].split(',')[2] + "," + trans22[index].split(',')[3] + "," + trans22[index].split(',')[4] + "," + trans22[index].split(',')[5] + "," + trans22[index].split(',')[6] + '\n')
                continue
            MT3.write(str(trans21[index].split(',')[0]) + "MT2," + str(trans21[index].split(',')[1]) + "," + str(trans21[index].split(',')[2]) + "," + str(trans21[index].split(',')[3]) + '\n')
            MT3.write(str(trans22[index].split(',')[0]) + "MT2," + str(trans22[index].split(',')[1]) + "," + str(trans22[index].split(',')[2]) + "," + str(trans22[index].split(',')[3]) + "," + str(trans22[index].split(',')[4]) + "," + str(trans22[index].split(',')[5]) + "," + str(trans22[index].split(',')[6]) + '\n')