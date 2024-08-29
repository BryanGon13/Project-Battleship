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

## Features

- Ships are randomly positioned on the board each time a new game begins, ensuring a unique experience with every playthrough.
- Player input is validated to ensure that all coordinates are within the bounds of the game board.
- The game prevents the player from targeting the same location more than once.

## Software Used

Below is a list of the software/applications used in the construction of this project:

- [GitHub](https://github.com/)
    - Used to store and manage the project's code.
- [Visual Studio Code](https://code.visualstudio.com/)
    - Used as the project's Integrated Development Environment (IDE).
- [Am I Responsive](https://ui.dev/amiresponsive)
    - Used to create an image of the various display sizes of the site.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy the application and host it online.

## Testing

### Game Testing

![Screenshot of opening statement](/assets/images/open_statement.png)

When you start the game, you will see a welcoming title, "Welcome to Battleships!", prominently displayed at the top of the terminal. This sets the stage for an exciting battle of strategy and skill.

The game is set up on a 5x5 grid representing the ocean where ships are hidden. There are 5 enemy ships, each occupying a single cell on the grid. Your mission is to find and sink all the ships using a maximum of 12 shots.

The coordinate system for the game is straightforward:

- Rows are numbered from 1 to 5.
- Columns are labeled from A to E.
- To make a move, enter the row number followed by the column letter (e.g., 3 B). This system helps you target specific grid locations for your shots.

![Are you ready?](/assets/images/ready.png)

### User Input: Are You Ready?

Before the game starts, you'll be prompted with a question: "Are you ready to play?". You can respond by typing "yes" or "no":

- If you type "yes", the game will begin, and you'll proceed to the gameplay screen where you can start guessing the locations of enemy ships.
- If you type "no", the system will acknowledge your response and wait for you to confirm when you're ready to start. You will need to type "yes" to begin the game.

### Handling Invalid Inputs

If you enter anything other than "yes" or "no", the system will display a message indicating that the input is invalid. It will then prompt you again with the question "Are you ready to play?" until a valid response is received. This ensures that the game only starts when the player is fully prepared and aware of the game rules.

![Invalid coordinates](/assets/images/invalid_coordinates.png)

During gameplay, you will be asked to enter the coordinates of your shot to try and hit an enemy ship. The input process is straightforward, but it's important to enter valid coordinates:

### Entering Coordinates

- Row Number: You must enter a row number between 1 and 5.
- Column Letter: You must enter a column letter between A and E.

### Invalid Coordinate Handling

If you enter a coordinate outside these ranges, such as a row number greater than 5 or a column letter outside of A to E, the system will detect the error and display a message indicating that the input is invalid. You will then be prompted to enter a valid row and column again.

![Hit](/assets/images/hit.png)

During the game, your objective is to guess the location of the hidden enemy ships on the 5x5 grid. When you correctly guess the location of a ship, it is considered a hit.

### What Happens When You Guess a Hit?

- If your guess is correct and you hit a ship, the game will immediately notify you with a message indicating a "Hit!".
- The grid will update to reflect your successful guess. The cell corresponding to the hit location will be marked with an 'O'. This mark signifies that a ship has been struck in that particular cell.
- The updated grid will be displayed, showing the hit mark. This allows you to keep track of successful shots and adjust your strategy accordingly.

### Game Progress After a Hit

- After each hit, the game will continue, allowing you to make your next guess.
- The goal is to hit all 5 enemy ships before running out of your 12 available shots. Each successful hit brings you closer to winning the game.
- If you successfully hit all the ships, the game will display a victory message, congratulating you on sinking all the enemy ships.

![gameover](/assets/images/gameover.png)

### Game Over

The game concludes when either all enemy ships have been sunk or you have used up all your available shots. Here’s what happens in each scenario:

- Sinking All Ships:

    - If you successfully hit all 5 enemy ships before exhausting your 12 shots, the game will display a congratulatory message indicating that you have won. This means you’ve outplayed the computer and completed your mission.

- Running Out of Shots:

    - If you use up all 12 shots without sinking all the enemy ships, the game will notify you with a "Game Over" message. This message will indicate that you’ve run out of shots and provide a summary of your performance, including how many ships were still afloat.

### End of Game Summary

- At the end of the game, regardless of the outcome, the final state of the grid will be displayed, showing all the remaining ships and hits.
- You will be given the option to play again or exit the game. If you choose to play again, the game will reset, and new ships will be placed randomly on the grid.

## Software Validation Testing

The code was tested using Code Institute's Python Linter for PEP8 compliance. The same error was identified:

- E501: Line too long — This issue occurs because some lines exceed the recommended length. This was done intentionally to center text and add borders for better readability and formatting.

These adjustments were made to enhance the visual layout of the output, and I have verified the code to ensure it functions as intended despite these formatting exceptions.

![pyhton linter](/assets/images/ci_pyhton_linter.png)

## Deployment

The project was deployed using GitHub pages. The steps to deploy using GitHub pages are:

1. Go to the repository on GitHub.com
2. Select 'Settings' near the top of the page.
3. Select 'Pages' from the menu bar on the left of the page.
4. Under 'Source' select the 'Branch' dropdown menu and select the main branch.
5. Once selected, click the 'Save'.
6. Deployment should be confirmed by a message on a green background saying "Your site is published at" followed by the web address.

The live link can be found here - [Battleship](https://project-battleship-38c990e11220.herokuapp.com/)

### Resources Used

- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Youtube](https://www.youtube.com/)
- [ChatGPT]

## Acknowledgments
My mentor Antonio for his support and advice.

The Code Institute slack community for their quick responses and very helpful feedback.