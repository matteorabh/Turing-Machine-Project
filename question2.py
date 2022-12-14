import question1


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
            elif ligne_2[i+nb_bande] == '<':
                MT.tete_lecture[i] -= 1
    else:
        print("Vous n'avez pas initialisé votre machine de Turing!")
        exit()

print(pas(question1.initialisation('kayak','MT_Donnee.txt')))