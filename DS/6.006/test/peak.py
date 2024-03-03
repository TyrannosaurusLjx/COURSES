import random as rd
import numpy as np

def creat_list():
    n = rd.choice([3,4,5,6,7,8])
    lst = [rd.randint(1,20) for i in range(n)]
    return lst

def find_peak(lst):
    n = len(lst)
    if lst[0] > lst[1]:
        return lst[0]
    elif lst[-1] > lst[-2]:
        return lst[-1]
    else:
        for i in range(1,n-1):
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                return lst[i]

def binary_find_peak(lst):
    n = len(lst)
    mid = int(n/2)
    if lst[0] > lst[1]:
        return lst[0]
    if lst[-1] > lst[-2]:
        return lst[-1]

    if lst[mid] < lst[mid-1]:
        return binary_find_peak(lst[:mid-1])
    elif lst[mid] < lst[mid+1]:
        return binary_find_peak(lst[mid+1:])
    else:
        return lst[mid]

def creat_matrix():
    m, n = rd.randint(2,10), rd.randint(2,10)
    mat = [[rd.randint(1,10) for i in range(m)] for j in range(n)]
    return np.array(mat)

def find_mat_peak(mat):
    m = len(mat)
    n = len(mat[0])
    j = int(n/2)
    i = np.argmax(mat[:,j])
    if mat[i,j-1] > mat[i,j]:
        return find_mat_peak(mat[i,:j])
    elif mat[i,j+1] > mat[i,j]:
        return find_mat_peak(mat[i,j+1:])
    else:
        return mat[i,j]




