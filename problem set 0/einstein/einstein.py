#Prompts the user to insert the mass in kg
mass = float(input("Insert the mass in kg: "))

#Calculates the energy using the formula E = mc^2
energy = mass * (3 * 10**8)**2
print(f"{energy:.0f}")

#Prints the energy in Joules
print("The energy is", energy, "Joules")
