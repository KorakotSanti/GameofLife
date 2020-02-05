""" Conway's Game of Life implementation
Team 1
"""
import os
from time import sleep
from sys import platform
from random import randint

# global variables for max row and max col
# so we do not need to pass the maxrow and maxcol to multiple functions
maxrow = 0
maxcol = 0

# count to count the generations of cells
count = 0

def display_array(arr):
    """
    The given starter function with slight modification to support our implementation
    """
    global count

    #check os first!
    if platform == "linux" or platform == "darwin":
        #this the way linux and macos clears terminal
        os.system("clear")
    elif platform == "win32":
        #this the way windows clears cmd/powershell
        os.system("cls")

    rows = len(arr)

    if not rows:
        raise ValueError("Array contains no data")

    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if(arr[i][j]):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    
    print("\n\n")
    count+= 1
    print(f'Generation: {count}')

    sleep(1)

def solution(input):
    """
    Function takes the array of cells and 
    return the next generations of cells with the rules applied to them

    Parameters
    ----------
    :param input:   The array of cells
    """
    # make a new array of same size which will represent the next generation
    result = [[0 for j in range(maxcol)] for i in range(maxrow)]

    for i in range(maxrow):
        for j in range(maxcol):
            # if live cell
            if input[i][j]:
                # check if live cell is still living
                if checkLivecell(input,i,j):
                    result[i][j] = 1
            else:
                # check if dead cells turn live cell
                if checkDeadcell(input,i,j):
                    result[i][j] = 1

    return result

def checkLivecell(input,crow,ccol):
    """
    returns True or False
    True means that the cells lives, False will indicate that cell dies

    Parameters
    ----------
    :param input:   the array of cells
    :param crow:    the row of the cell we are looking at
    :param ccol:    the col of the cell we are looking at
    """
    live = 0

    # first check if to see if not out of bounds before
    # checking the neighbors starting from top left diagonal
    # going clockwise
    # after the third if statment would start checking if count exceeds 3
    if crow-1 >= 0 and ccol-1 >= 0:
        if input[crow-1][ccol-1]:
            live+=1

    if crow-1 >= 0:
        if input[crow-1][ccol]:
            live+=1

    if crow-1 >=0 and ccol+1 < maxcol:
        if input[crow-1][ccol+1]:
            live+=1

    if ccol+1 < maxcol:
        if input[crow][ccol+1]:
            live+=1
        if live > 3:
            return False

    if crow+1 < maxrow and ccol+1 < maxcol:
        if input[crow+1][ccol+1]:
            live+=1
        if live > 3:
            return False
    
    if crow+1 < maxrow:
        if input[crow+1][ccol]:
            live+=1
        if live > 3:
            return False
    
    if crow+1 < maxrow and ccol-1 >= 0:
        if input [crow+1][ccol-1]:
            live+=1
        if live > 3:
            return False
    
    if ccol-1 >=0:
        if input[crow][ccol-1]:
            live+=1
        if live > 3:
            return False
    
    # check if cell lives
    if count == 2 or count == 3:
        return True

    return False

def checkDeadcell(input,crow,ccol):
    """
    Function to check the Dead cell rules
    returns True if dead cell turns to live cell or False if dead cells stays dead cells

    Parameters
    ----------
    :param input:   the array of cells
    :param crow:    the row of the cell we are looking at
    :param ccol:    the col of the cell we are looking at
    """
    live = 0

    # first check if to see if not out of bounds before
    # checking the neighbors starting from top left diagonal
    # going clockwise
    # after the third if statment would start checking if count exceeds 3
    if crow-1 >= 0 and ccol-1 >= 0:
        if input[crow-1][ccol-1]:
            live+=1

    if crow-1 >= 0:
        if input[crow-1][ccol]:
            live+=1

    if crow-1 >=0 and ccol+1 < maxcol:
        if input[crow-1][ccol+1]:
            live+=1

    if ccol+1 < maxcol:
        if input[crow][ccol+1]:
            live+=1
        if live > 3:
            return False

    if crow+1 < maxrow and ccol+1 < maxcol:
        if input[crow+1][ccol+1]:
            live+=1
        if live > 3:
            return False

    if crow+1 < maxrow:
        if input[crow+1][ccol]:
            live+=1
        if live > 3:
            return False

    if crow+1 < maxrow and ccol-1 >= 0:
        if input [crow+1][ccol-1]:
            live+=1
        if live > 3:
            return False

    if ccol-1 >= 0:
        if input[crow][ccol-1]:
            live+=1
        if live > 3:
            return False

    #check if the dead cell will turn to live cell
    if live == 3:
        return True

    return False

def generateCells():
    """
    This function generates random all cells randomly
    0 representing dead cells and 1 representing live cells
    """
    return [[randint(0,1) for j in range(maxcol)] for i in range(maxrow)]

def main(row,col,generations):
    """
    main function to run the whole program

    Parameters
    ----------
    :param row:         number of row in the array
    :param col:         number of col in the array
    :param generations: The number of generations of cells to display
    """
    global maxrow, maxcol, count

    count = 0

    # the args get maxrow and maxcol
    maxrow = row
    maxcol = col

    # generate the intiate cells boards
    inputarr = generateCells()
    #display the cells board
    display_array(inputarr)

    # get the next n-1 generations because the initial cells board
    # was technically the 1st generation
    for i in range(generations-1):
        inputarr = solution(inputarr)
        display_array(inputarr)
