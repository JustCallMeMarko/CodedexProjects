from math import pi
def Menu():
    print("""
==================
Area Calculator 📐
==================

1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit""")

def triangle():
    print()
    Height = int(input("Height: "))
    Base = int(input("Base: "))

    area = (Height*Base)/2
    print()
    print(f"The area is {area:.2f}")

def rectangle():
    print()
    Length = int(input("Length: "))
    Width = int(input("Width: "))

    area = Length * Width
    print()
    print(f"The area is {area:.2f}")

def square():
    print()
    Side = int(input("Side: "))

    area = Side**2
    print(f"The area is {area:.2f}")

def circle():
    print()
    Radius = int(input("Radius: "))

    area = pi*(Radius**2)
    print()
    print(f"The area is {area:.2f}")

def main():
    while True:
        Menu()
        print()
        shape = input("Which shape: ")
        match(shape.lower()):
            case "triangle":
                triangle()
            case "rectangle":
                rectangle()
            case "square":
                square()
            case "circle":
                circle()
            case "quit":
                print("Exiting...")
                break

main()
