#GSÖ py

skra = input("Sláðu inn nafn skáar: ")
nafnSkra = skra + ".txt"
skrainMin = open(nafnSkra, "w+")
skrainMin.close()

print("Skrifaðu nú í skránna")

skrainMin = open(nafnSkra, "a")
lina1 = input("Fyrsta línan í skránni: "+"\n")
lina2 = input("Seinni línan í skránni: "+"\n")
lina3 = input("Þriðja línan í skránni: "+"\n")
lina4 = input("Fjórða línan í skránni: "+"\n")
skrainMin.write(lina1 + "\n")
skrainMin.write(lina2 + "\n")
skrainMin.write(lina3 + "\n")
skrainMin.write(lina4 + "\n")
skrainMin.close()
skrainMin = open(nafnSkra, "r")
innihald = skrainMin.read()
print(innihald)
skrainMin.close()