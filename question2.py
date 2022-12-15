from question1 import initialisation


def allonge_bande(liste,binaire):
    """
    Permet d'aggrandir la bande. 
    Ajoute un _ à la fin de la liste si la tête de lecture avance. 
    Ajoute un _ au début de la liste si la tête de lecture recule. 
    """
    if binaire == 0:
        l = ['_'] 
        l.extend(liste)
        return l 
    else:
        return liste.append('_')

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
        ligne_2 = MT.transitions[ligne_1].split(',')

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

#pas(initialisation('1010','MT_Donnee.txt'))
