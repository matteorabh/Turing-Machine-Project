import question1


def allonge_bande(liste,binaire):
    if binaire == 0:
        l = ['_'] 
        for elem in liste:
            l.append(elem)
        return l 
    else:
        return liste.append('_')

def pas(MT):  
    if MT.transitions != False:
        nb_bande = MT.nb_bande
        ligne_1 = MT.etat

        #recupération données
        for i in range(1,nb_bande+1):
            ligne_1 += ',' + MT.etat_bande[i][MT.tete_lecture[i]]
        ligne_2 = MT.transitions[ligne_1].replace(',','')

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

pas(question1.initialisation('1010','MT_Donnee.txt'))