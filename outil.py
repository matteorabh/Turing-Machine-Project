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
    etats = [lines[i][0] for i in range(0,len(lines),2)]
    if 'I' not in etats:
        raise EnvironmentError("Il manque l'état initial I")
    if 'F' not in etats:
        raise EnvironmentError("Il manque l'état initial F")
    else:
        return True

def verif_determinisme():
    return

def verif_binaire():
    return