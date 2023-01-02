from main import initialisation, assemble_machines, simulation_precise

MT1 = initialisation("", "MT_mult_egyptienne1.txt")
MT2 = initialisation("", "MT_Addition.txt")
assemble_machines(MT1, MT2)
MT3 = initialisation("110*11", "MT3.txt")
simulation_precise("110*11", MT3)