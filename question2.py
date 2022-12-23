from main import initialisation,pas

print()
M = initialisation('1010','MT_Donnee.txt')
print("Etat initial :\n")
M.element()
print("\n\n")
pas(M)
print("Etat apres un pas :\n")
M.element()
print()