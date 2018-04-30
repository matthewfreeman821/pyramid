def pyramid(numLines):

    row = 0

    while(row < numLines):
        row += 1
        spaces = numLines - row
        spacesCounter = 0

        while(spacesCounter < spaces):
            print(" ", end='')
            spacesCounter += 1

        numStars = 2*row-1
        while(numStars > 0):
            print("*", end='')
            numStars -= 1

        print()
    return numLines