from main import initialisation,simulation_precise

print()
print("Machine : LEFT")
M1 = initialisation('1010','MT_LEFT.txt')
simulation_precise('1111',M1)

print("Machine : SEARCH")
M2 = initialisation('1010','MT_SEARCH.txt')
simulation_precise('0010',M2)

print("Machine : ERASE")
M3 = initialisation('1010','MT_ERASE.txt')
simulation_precise('1111',M3)

print("Machine : COPY")
M4 = initialisation('1010','MT_COPY.txt')
simulation_precise('1111',M4)
print()