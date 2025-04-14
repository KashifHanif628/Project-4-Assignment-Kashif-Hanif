# 🔍 Problem Samajhna
# NASA ne Mars par ek chhota helicopter (Ingenuity) udaaya jo Python ka use karta hai. Kyun ke Mars ki gravity Earth se kam hai, wahan koi bhi cheez halki mehsoos hoti hai.

# ✅ Milestone #1: Sirf Mars par weight calculate karna
# Agar hamara weight Earth par 100 kg hai, to Mars par ye 37.8% hoga, yaani 100 * 0.378 = 37.8 kg.

# mars_weight = earth_weight * 0.378
# Phir use 2 decimal places tak round karna hai:

# rounded = round(mars_weight, 2)
# ✅ Milestone #2: Har planet ke liye weight calculate karna
# Har planet ka alag gravitational ratio hota hai:

# Planet	Gravity (%)
# Mercury	37.6
# Venus	    88.9
# Mars	    37.8
# Jupiter	236.0
# Saturn	108.1
# Uranus	81.5
# Neptune	114.0

# hame user se:
# Earth ka weight lena hai
# Planet ka naam lena hai
# Wahan ka weight calculate karke dikhana hai (rounded to 2 decimals)

def main():
    # Step 1: Get user's Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Step 2: Get the planet name
    planet = input("Enter a planet: ")

    # Step 3: Define gravity factors
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Step 4: Calculate weight on selected planet
    if planet in gravity_factors:
        planet_weight = earth_weight * gravity_factors[planet]
        planet_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

# Run the function
if __name__ == '__main__':
    main()