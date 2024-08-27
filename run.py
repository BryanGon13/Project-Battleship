# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

def print_landing_page():
    """Display the landing page for the Battleships game."""
    print("-" * 60)
    print("Welcome to Battleships!")
    print("-" * 60)
    print("Prepare to test your strategic skills in this classic game of Battleships.")
    print()
    print("Game Mode:")
    print("  - Player vs Computer")
    print()
    print("Game Setup:")
    print("  - Board Size: 5x5")
    print("  - Total Number of Ships: 5 (Each ship occupies one cell)")
    print()
    print("Coordinate System:")
    print("  - The board is indexed from (A to E) for colum and (1 to 5) for rows")
    print("  - Enter coordinates in the format: row column")
    print()
    print("How to Play:")
    print("  - You will have 12 shots to sink all ships.")
    print("  - A 'O' indicates a hit which means you’ve struck a ship!")
    print("  - A 'X' indicates a miss which means the shot did not hit any ship.")
    print()
    print("Objective:")
    print("  - Sink all 5 ships before running out of shots.")
    print()
    print("Good luck!")
    print("-" * 60)


def create_grid(size=5):
    """Create a 5x5 grid."""
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    """Print the game grid with column labels A-E and row labels 1-5, hiding ships."""
    size = len(grid)
    
    # Print column headers (A-E)
    column_labels = "  " + "   ".join(chr(65 + i) for i in range(size))  # chr(65) is 'A'
    print(column_labels)
    
    # Print rows with row numbers (1-5)
    for idx, row in enumerate(grid):
        row_label = str(idx + 1)  # Convert row number to 1-based index
        # Replace 'S' with a space ' ' to hide the ships
        row_data = " | ".join(cell if cell in ['O', 'X'] else ' ' for cell in row)
        print(f"{row_label} | {row_data} |")
        print("  " + "---|---|---|---|---")  # Add a horizontal separator for each row

    print()

def place_ships(grid, num_ships=5):
    """Place ships randomly on the grid."""
    size = len(grid)
    ships_placed = 0
    
    while ships_placed < num_ships:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        
        # Only place a ship if the cell is empty
        if grid[x][y] == ' ':
            grid[x][y] = 'S'  # 'S' represents a ship
            ships_placed += 1






