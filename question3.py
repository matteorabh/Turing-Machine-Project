from question2 import pas

def simulation(mot,MT):
    MT.etat_bande[0] = [lettre for lettre in mot]
    while MT.etat != 'F':
        pas(MT)
        
