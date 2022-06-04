import numpy as np

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# transposes the 2D list using np.array 
def transpose(tableData):
    t = np.array(tableData).T
    return t.tolist()

# print table function
def printTable(tableData):
    t1 = transpose(tableData)
    # make column as long as number of transpose columns
    longest_col = [0] * len(t1[0])
    # finds max length of all columns
    for idx, _ in enumerate(t1):
        for idx2,j in enumerate(t1[idx]):
            if(len(str(j)) > longest_col[idx2]):
                longest_col[idx2] = len(j)
    print(longest_col)
    
    # prints out the right adjusted columns
    for idx1, _ in enumerate(t1):
        for idx2, _ in enumerate(t1[idx1]):
            print(t1[idx1][idx2].rjust(longest_col[idx2]), end = " ")
        print("")

printTable(tableData)
