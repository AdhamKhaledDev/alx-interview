#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''
from math import factorial
def pascal_triangle(n):
    if n <= 0:
        return []  

    result = []  
    for row in range(n):
        current_row = []  
        for col in range(row + 1):
            
            coefficient = factorial(row) // (factorial(col) * factorial(row - col))
            current_row.append(coefficient) 
        result.append(current_row)  

    return result