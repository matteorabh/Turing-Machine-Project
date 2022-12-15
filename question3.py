from question2 import pas
from question1 import initialisation

def simulation(mot,MT):
    """
    Simule l'avancée d'une machine de Turing jusqu'à ce que l'état final soit trouvé 
    ou lorsque l'état cherché n'existe pas. 
    """
    MT.etat_bande[1] = [lettre for lettre in mot]
    while MT.etat != 'F':
        pas(MT)
    print()
    print('La simulation de la machine de Turing est terminé !')
    print()
        
#simulation('110',initialisation('1010','MT_Donnee.txt'))