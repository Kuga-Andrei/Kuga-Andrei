def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    # Directions: up, down, left, right, and diagonals
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue  # Skip mines
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count