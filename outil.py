# verif alphabet conforme
# verif deterministe

def supp_n(lines):
    """
    Fonction qui supprime les \n d'une liste
    (Utile après le stockage du fichier)
    """
    return [lines[i].rstrip('\n').replace(' ','') for i in range(len(lines)) if lines[i] != '\n']

def verif_etat_initial_final(fichier):
    with open(fichier) as f:
        lines = supp_n(f.readlines())
    etats = {lines[i][0] for i in range(len(lines))}
    if 'I' not in etats:
        print("Il manque l'état initial I")
        exit()
    if 'F' not in etats:
        print("Il manque l'état initial F")
        exit()
    else:
        return True

def verif_determinisme(fichier, transitions):
    ligne = []
    with open(fichier) as f :
        lines = supp_n(f.readlines())
        for i in range(1, len(lines)-1, 2) :
            ligne = lines[i].split(',')
            print([list(transitions.keys())[i].split(',')[0] for i in range(len(transitions))])
            print(str(ligne[0]))
            if str(ligne[0]) in [list(transitions.keys())[i].split(',')[0] for i in range(len(transitions))] or ligne[0] == "F" :
                pass
            else :
                print("La machine de Turing est incorrecte car la nouvelle transition ne pourra jamais être lue.")
                exit()
    return True

def verif_binaire():
    return