# Battleship

"Battleships" is a classic game of strategy and tactics where the player takes on the challenge of sinking enemy ships. In this version, you will engage in a battle against a computer opponent on a 5x5 grid, aiming to locate and destroy all enemy ships hidden on the board.

The live link can be found here - [Battleship](https://project-battleship-38c990e11220.herokuapp.com/)

![Battleship Am I Responsive Image](/assets/images/responsive.png)

## User Experience (UX) & Design

For this project, the user interface is designed to be intuitive and engaging, even within the constraints of a command-line interface. The goal is to provide a visually appealing experience through clear text formatting. Key information is centered on the screen to make it stand out, and text effects are used sparingly to enhance readability without overwhelming the user.

To achieve a more polished look, spaces and line breaks are carefully placed to center important messages and actions. This approach creates a clean and organized appearance, guiding the user's attention to critical parts of the game, such as instructions, prompts, and game outcomes.

### User Stories

As a player, I want the game to provide the following features:

- A visible title at the top of the screen to identify the application.
- Display of instructions at the start of the game to guide gameplay.
- A game board that shows where I can make my guesses.
- A visual record of all my previous shots on the game board.
- Immediate feedback on whether each of my shots was a hit or miss.
- A counter showing the number of remaining shots I have left.

### Gameplay

When the game starts, the title and instructions are displayed in the terminal, followed by the player's 'guess' board. This board shows the positions of all previous shots, and any hits on enemy ships will be marked.

- The player is prompted to enter a row number between 1 and 5 for their shot.
    - If the input is outside this range (less than 1 or greater than 5), the player will be asked to enter a valid row number again.
- The player is then asked to enter a column letter between A and E.
    - If the input is not a letter between A and E, the player will be prompted to enter a valid column letter again.
- After each shot, the player is informed whether it was a "Hit" or a "Miss."
- The player is also updated on the number of remaining shots out of a total of 12.
- The game continues until either all 5 enemy ships are sunk or the player runs out of shots.
- At the end of the game, a message will be displayed indicating whether the player has won by sinking all the ships or lost by exhausting all their shots.

