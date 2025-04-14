C: int = 299792458  

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    main()


# created the 2nd programme

# Define the speed of light as a constant
C: int = 299792458  # Speed of light in meters per second

def main():
    # Get mass input from the user
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    
    # Step 1: Calculate C squared i.e 299792458 * 299792458 = 8.987551787368176e+16 which is squared of C (speed of energy)
    c_squared: float = C ** 2
    print(f"C^2 = {C}^2 = {c_squared}")
    
    # Step 2: Multiply mass with C squared i.e
    # if user mass input 100 in kg then multiply it by * 8.987551787368176e+16 = 8.987551787368176e+18 which is energy_in_joules.
    energy_in_joules: float = mass_in_kg * c_squared
    print(f"E = m * C^2 = {mass_in_kg} * {c_squared} = {energy_in_joules}")
    
    # Display results as per the requirement.
    print("\ne = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# Run the main function
if __name__ == '__main__':
    main()



# create the 3rd programme
C = 299792458  # Speed of Light in m/s

def main():
    mass = float(input("Enter mass in kg: "))
    energy = mass * (C ** 2)
    print("e = m * C^2...")
    print("m =", mass, "kg")
    print("C =", C, "m/s")
    print(energy, "joules of energy!")

if __name__ == '__main__':
    main()