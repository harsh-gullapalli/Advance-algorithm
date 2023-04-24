import sys
from itertools import permutations

def tsp(dist):
    n = len(dist)
    perms = permutations(range(1, n))
    min_distance = sys.maxsize
    
    for perm in perms:
        perm = (0,) + perm + (0,)
        distance = 0
        current_node = perm[0]
        
        for i in range(1, n+1):
            next_node = perm[i]
            distance += dist[current_node][next_node]
            current_node = next_node
        
        min_distance = min(min_distance, distance)
    
    return min_distance

dist = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

print("Minimum cost of the travel is",tsp(dist))  
