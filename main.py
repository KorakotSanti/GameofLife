import os
from time import sleep

def display_array(arr):
    os.system("clear")
    rows = len(arr)

    if not rows:
        raise ValueError("Array contains no data")

    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=' ')
        print()
    
    sleep(1)

def solution(row,col,input,gen):
    result = [[0 for j in range(col)] for i in range(row)]

    for i in range(row):
        for j in range(col):
            # live cell
            if input[i][j]:
                if checkLivecell(input,i,j,row,col):
                    result[i][j] = 1
                else:
                    result[i][j] = 0
            else:
                if checkDeadcell(input,i,j,row,col):
                    result[i][j] = 1
                else:
                    result[i][j] = 0

    return result

def checkLivecell(input,crow,ccol,row,col):
    """
    crow = current row
    ccol = current col
    row = length of the row
    col = length of the col
    """
    count = 0

    if crow-1 >= 0 and ccol-1 >= 0:
        if input[crow-1][ccol-1]:
            count+=1
    if crow-1 >= 0:
        if input[crow-1][ccol]:
            count+=1
    if crow-1 >=0 and ccol+1 < col:
        if input[crow-1][ccol+1]:
            count+=1
    if ccol+1 < col:
        if input[crow][ccol+1]:
            count+=1
        if count > 3:
            return False
    if crow+1 < row and ccol+1 < col:
        if input[crow+1][ccol+1]:
            count+=1
        if count > 3:
            return False
    
    if crow+1 < row:
        if input[crow+1][ccol]:
            count+=1
        if count > 3:
            return False
    
    if crow+1 < row and ccol-1 >= 0:
        if input [crow+1][ccol-1]:
            count+=1
        if count > 3:
            return False
    
    if ccol-1 >=0:
        if input[crow][ccol-1]:
            count+=1
        if count > 3:
            return False
    
    if count < 2:
        return False

    return True
    


def checkDeadcell(input,crow,ccol,row,col):
    """
    crow = current row
    ccol = current col
    row = length of the row
    col = length of the col
    """
    count = 0

    if crow-1 >= 0 and ccol-1 >= 0:
        if input[crow-1][ccol-1]:
            count+=1
    if crow-1 >= 0:
        if input[crow-1][ccol]:
            count+=1
    if crow-1 >=0 and ccol+1 < col:
        if input[crow-1][ccol+1]:
            count+=1
    if ccol+1 < col:
        if input[crow][ccol+1]:
            count+=1
    if crow+1 < row and ccol+1 < col:
        if input[crow+1][ccol+1]:
            count+=1
    
    if crow+1 < row:
        if input[crow+1][ccol]:
            count+=1

    if crow+1 < row and ccol-1 >= 0:
        if input [crow+1][ccol-1]:
            count+=1

    if ccol-1 >=0:
        if input[crow][ccol-1]:
            count+=1
    
    if count == 3:
        return True

    return False