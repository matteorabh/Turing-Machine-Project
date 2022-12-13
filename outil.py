# verif alphabet conforme
# verif deterministe

def supp_n(lines):
    """
    Fonction qui supprime les \n d'une liste
    (Utile après le stockage du fichier)
    """
    return [lines[i][:lines[i].find('\n')] for i in range(len(lines)) if lines[i] != '\n']

def verif_etat():
    return

def verif_determinisme():
    return

def verif_binaire():
    return