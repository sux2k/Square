#Square of x => x * x => x ^ 2

print("This script return a square of a number")

x = int(input("Please, enter the number: "))

def Square(x):

    Square = x * x
    return(Square)

print("The square of", x, "is", Square(x))