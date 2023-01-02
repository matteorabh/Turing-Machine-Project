from main import initialisation, assemble_machines, simulation_precise

MT1 = initialisation("", "MT_Tri.txt")
MT2 = initialisation("", "MT_Comparaison.txt")
assemble_machines(MT1, MT2)
MT3 = initialisation("11#10#11", "MT3.txt")
simulation_precise("11#10#11", MT3)