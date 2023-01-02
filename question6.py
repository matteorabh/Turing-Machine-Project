from main import initialisation, assemble_machines, simulation_precise

MT1 = initialisation("0100", "MT_mult_egyptienne1.txt")
assemble_machines("0100", MT1)
MT3 = initialisation("0100", "MT3.txt")
simulation_precise("110*11", MT3)