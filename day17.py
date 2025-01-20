import heapq

def minimumHeatLoss(grid):
    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Min-heap for Dijkstra's algorithm
    pq = []
    heapq.heappush(pq, (0, 0, 0, -1))  # (heat_loss, x, y, direction) where direction is -1 (no direction)
    
    # Visited set to track visited positions with a specific direction
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]
    
    while pq:
        heat_loss, x, y, direction = heapq.heappop(pq)

        # If we have reached the bottom-right corner, return the heat loss
        if x == rows - 1 and y == cols - 1:
            return heat_loss
        
        # Mark the current position and direction as visited
        if visited[x][y][direction + 1]:
            continue
        visited[x][y][direction + 1] = True
        
        # Try all four directions
        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols:
                # Compute the new heat loss
                new_heat_loss = heat_loss + grid[new_x][new_y]
                
                # If we are moving in the same direction, check if we have already moved 3 steps
                if direction == i:
                    heapq.heappush(pq, (new_heat_loss, new_x, new_y, i))
                else:
                    heapq.heappush(pq, (new_heat_loss, new_x, new_y, i))

    return -1  # If we could not find a path (though unlikely)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = [list(map(int, line.split())) for line in file]
    result = minimumHeatLoss(grid)
    print("Minimum heat loss:", result)
