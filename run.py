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
    print("  - Rows are numbered from 1 to 5.")
    print("  - Columns are labeled from A to E.")
    print("  - Enter your move in the format: row column (e.g., 3 B)")
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
            grid[x][y] = 'S'  # 'S' represents a ship internally
            ships_placed += 1

def make_guess(grid, x, y):
    """Process a guess and update the grid."""
    if grid[x][y] == 'S':
        grid[x][y] = 'O'  # Hit
        return True
    elif grid[x][y] == ' ':
        grid[x][y] = 'X'  # Miss
        return False
    else:
        return None  # Already guessed

def get_user_ready():
    """Prompt the user to start the game."""
    ready = input("Are you ready to play? (yes/no): ").strip().lower()
    while ready != 'yes':
        if ready == 'no':
            print("Okay, take your time. Type 'yes' when you're ready.")
        else:
            print("Invalid input. Please type 'yes' when you're ready to play.")
        ready = input("Are you ready to play? (yes/no): ").strip().lower()

def play_game():
    """Start and run a single game of Battleships."""
    size = 5
    grid = create_grid(size)
    place_ships(grid)

    print("Game has started!")
    print_grid(grid)  # Show the initial grid (with hidden ships)

    shots_taken = 0
    max_shots = 12

    while shots_taken < max_shots:
        try:
            x = int(input("Enter row (1-5): ")) - 1  # Adjust for 0-based indexing
            y = input("Enter column (A-E): ").upper()

            # Convert column input to index
            if y in 'ABCDE':
                y = ord(y) - 65  # Convert A-E to 0-4
            else:
                raise ValueError("Invalid column input")

        except ValueError:
            print("Invalid input. Please enter a valid row and column.")
            continue

        if x < 0 or x >= size or y < 0 or y >= size:
            print("Invalid coordinates. Please enter values between 1-5 for rows and A-E for columns.")
            continue

        result = make_guess(grid, x, y)

        if result is None:
            print("You already guessed that location.")
        elif result:
            print("Hit!")
            if all(cell != 'S' for row in grid for cell in row):
                print("Congratulations! You've sunk all the ships!")
                break
        else:
            print("Miss!")

        shots_taken += 1
        print(f"You have {max_shots - shots_taken} shots left.")
        print_grid(grid)  # Show the updated grid after each guess

    if shots_taken >= max_shots:
        print("Game Over! You've used all your shots.")

def main():
    """Main function to control the flow of the game."""
    print_landing_page()  # Show the landing page

    # Ask user if they are ready to play
    get_user_ready()

    while True:
        play_game()  # Play a single game

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing Battleships! Goodbye!")
            break  # Exit the game loop if the user doesn't want to play again

if __name__ == "__main__":
    main()