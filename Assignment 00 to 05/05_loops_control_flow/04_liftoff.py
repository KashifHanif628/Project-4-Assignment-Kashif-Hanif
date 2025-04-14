# ek esa program likhna hai jo spaceship ke launch se pehle countdown print kare:
# 10 9 8 7 6 5 4 3 2 1 Liftoff!

# Matlab:
# Pehle 10 se 1 tak reverse counting print karni hai.
# Phir "Liftoff!" print karna hai.

# For Loop ka basic concept:
# for i in range(10):
#    print(i)

# Ye code 0 se 9 tak print karega. Kyun? Kyunki range(10) ka matlab hota hai:
# [0, 1, 2, ..., 9]
# Lekin humein chahiye: [10, 9, 8, ..., 1]
# Iska matlab humein range() function ko thoda modify karna padega.

def main():

    for i in range(10, 0, -1):
        print(i, end=' ')
    print("Liftoff!")

if __name__ == '__main__':
    main()