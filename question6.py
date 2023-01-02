from main import initialisation, assemble_machines, simulation_precise

MT1 = initialisation("", "MT_RIGHT.txt")
MT2 = initialisation("", "MT_LEFT.txt")
assemble_machines(MT1, MT2)
MT3 = initialisation("110110", "MT3.txt")
simulation_precise("110110", MT3)