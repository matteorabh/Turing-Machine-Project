
def supp_n(lines):
    """
    Fonction qui supprime les \n d'une liste
    (Utile après le stockage du fichier)
    """
    return [lines[i].rstrip('\n').replace(' ','') for i in range(len(lines)) if lines[i] != '\n']

def verif_etat_initial_final(fichier):
    """
    Permet de vérifier les noms de l'état initial et final.
    """
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

def verif_determinisme(fichier):
    """
    Fonction qui permet de vérifier que le code de la Machine de Turing 
    est celui d'une MT déterministe.
    """
    with open(fichier) as f :
        lines = supp_n(f.readlines())
    liste = [lines[i] for i in range(0,len(lines),2)]
    ensemble = {lines[i] for i in range(0,len(lines),2)}
    if sorted(liste) != sorted(list(ensemble)):
        print("La machine de Turing est incorrecte car il existe deux fois la même transitions partant d'un même état.")
        exit()
    return True

def verif_alphabet(fichier, nb_bandes):
    """
    Permet de vérifier que l'alphabet du code est bien celui requis.
    """
    with open(fichier) as f:
        lines = supp_n(f.readlines())
    for line in lines:
        for index in range(1,nb_bandes+1):
            if line.split(',')[index] not in ["1", "0", "_"]:
                print("La machine de Turing est incorrecte car l'alphabet n'est pas correcte!")
                exit()
    return True

def verif_decalage(fichier, nb_bandes):
    """
    Permet de vérifier que le décalage indiqué après chaque transition est conforme.
    """
    with open(fichier) as f :
        lines = supp_n(f.readlines())
    for i in range(1, len(lines), 2):
        ligne = lines[i].split(',')
        for elem in ligne[nb_bandes+1:]:
            if elem not in [">", "<", "-"]:
                print("La machine de Turing est incorrecte car la syntaxe de décalage des bandes est incorrecte!")
                exit()
    return True