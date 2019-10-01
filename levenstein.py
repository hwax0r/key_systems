import numpy as np

def lev_dist(str1, str2):
    if str1 == "": return len(str2)
    if str2 == "": return len(str1)
    if str1[-1] == str2[-1]: val = 0
    else: val = 1
    result = min([lev_dist(str1[:-1], str2)+1, lev_dist(str1, str2[:-1])+1,
               lev_dist(str1[:-1], str2[:-1]) + val])
    return result

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y
        
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1)
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1)
    print (matrix)
    return (int(matrix[size_x - 1, size_y - 1]))



a = 'secold'
b = 'second'
print(levenshtein(a, b))
print(lev_dist(a, b))
