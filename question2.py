import question1


def pas(MT):
    with open("MT_Donnee.txt") as f:
        lines = f.readlines()

    cpt, liste, instructions = 0, [], []
    for line in lines:
        indice = line.find('\n')
        if line != '\n' and indice != -1:
            cpt += 1
            line = line[:indice]
            liste.append(line + ';')
        if cpt == 2:
            instructions.append(liste[:])
            liste.clear()
            cpt = 0

    for instruction in instructions:
        line = instruction[0] + instruction[1]
        indice = line.find(MT.etat)
        if indice != -1:
            liste = line.split(';')
            
            # état courant
            etat = liste[1].split(',')[0]

            # tête de lecture
            split = liste[1].split(',')[2]
            if split.find('>') != -1:
                tete_lecture = MT.tete_lecture + 1
            elif split.find('<') != -1:
                tete_lecture = MT.tete_lecture - 1
            else:
                tete_lecture = MT.tete_lecture 

            # état de la bande
            modif_bande = liste[1].split(',')[1]
            MT.etat_bande[tete_lecture] = modif_bande

            return question1.MT(etat,MT.etat_bande,tete_lecture)

print(pas(question1.initialisation(mot='1010')))