# island_perimeter

The island_perimeter(grid) function calculates the perimeter of an island represented in a given grid. The grid is a rectangular list of lists, where each cell can either represent land (1) or water (0). The function takes into account the connections between cells to determine the perimeter of the island.

# Usage

```python
grid = [
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
]
perimeter = island_perimeter(grid)
print(perimeter)
```
