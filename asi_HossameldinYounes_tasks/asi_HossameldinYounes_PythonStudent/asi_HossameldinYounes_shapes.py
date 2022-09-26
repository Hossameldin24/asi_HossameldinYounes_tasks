def drawpyramid(height):
    i = 1
    while i <= height:
        for n in range(height-i):
            print(" ", end='')
        for n in range(2*i-1):
            print("*", end='')
        for n in range(height-i-1):
            print(" ", end='')
        print(" \n", end='')
        i += 1


def drawsquare(height):
    i = 1
    while i <= height:
        for j in range(height):
            if j == 0 or j == height - 1 or i == 1 or i == height:
                print("* ", end='')
            else:
                print("  ", end='')
        print("\n", end='')
        i += 1


def drawtriangle(height):
    i = 1
    while i <= height:
        for j in range(i):
            if j == 0 or j == i - 1 or i == height:
                print("* ", end='')
            else:
                print("  ", end='')
        print("\n", end='')
        i += 1


def drawcircle(height):
    d = height - 1
    for x in range(height):
        for y in range(0, -1 * height, -1):
            if (x - d / 2) * 2 + (y + d / 2) * 2 <= (d / 2) ** 2 + 1:
                print("*", end='')
            else:
                print(" ", end='')
            print(" ", end='')
        print("\n", end='')

nextshape = True
while nextshape == True:
    wanted = input("Enter the wanted shape: ")
    
    while wanted != "triangle" and wanted != "square" and wanted != "circle" and wanted != "pyramid":
        print("Invalid shape")
        wanted = input("Enter the wanted shape: ")
    
        
    if wanted == "triangle":
        height = int(input("Enter triangle height: "))
    elif wanted == "circle":
        height = int(input("Enter circle diameter: "))
    elif wanted == "square":
        height = int(input("Enter side length: "))
    elif wanted == "pyramid":
        height = int(input("Enter pyramid height: "))
        
    if wanted == "triangle":
        drawtriangle(height)
    elif wanted == "circle":
        drawcircle(height)
    elif wanted == "square":
        drawsquare(height)
    elif wanted == "pyramid":
        drawpyramid(height)
        
    another = input("Do you want another shape? ")
    
    if another == "yes":
        nextshape = True
    else:
        nextshape = False


