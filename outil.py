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

def verif_determinisme():
    return

def verif_binaire():
    return