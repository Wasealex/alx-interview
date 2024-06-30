#!/usr/bin/python3
"""modul pascal trialgle"""
if __name__ == "__main__":
    """run directly"""
    def pascal_triangle(n):
        """def of pascal trialngle
        return list of lists of n triangle
        return empty if n < 0
        
        """
        if n <= 0:
            return []
        return [n] 
