#!/usr/bin/python3
"""modul pascal trialgle"""
if __name__ == "__main__":
    """run directly"""
    def pascal_triangle(n):
        """def of pascal trialngle
        return list of lists of n triangle
        return empty if n < 0
        
        """
        pascal = []
        if n <= 0:
            return pascal
        
        
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)
        
        return pascal
