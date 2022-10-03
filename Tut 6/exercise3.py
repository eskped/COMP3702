import numpy as np
gencar = -40000 + 330*(175-25) - 30*35
tesla1 = -120000 + 0.75*330*(500-10) - 0.75*30*35 + 0.25*(330*-5 - 35*(30+5))
tesla2 = np.array([-140000, 600*330*0.75, -10*300*0.75, -30*35])

print("Profit for 5 gencars:", gencar*5)
print("Profit for 2 Tesla Model x without upgrade:", tesla1*2)
print("Profit for 2 Tesla Model x with upgrade:", np.sum(tesla2)*2)
