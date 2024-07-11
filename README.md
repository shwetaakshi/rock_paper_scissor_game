# Rock Paper Scissor Game

This repository contains a simple implementation of the classic Rock, Paper, Scissors game using Python. The game allows a player to choose between rock, paper, and scissors, while the computer randomly selects its choice. The winner is determined based on the standard rules of the game.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/rock_paper_scissor_game.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd rock_paper_scissor_game
   ```

## Usage

Run the script to start the game. You will be prompted to enter your choice (rock, paper, or scissors), and the computer will randomly select its choice. The result of the game will be displayed on the screen.

```sh
python rock_paper_scissor_game.ipynb
```

## Code Overview

The script consists of three main functions:

1. **`get_choices()`**: This function prompts the player to enter their choice and randomly selects a choice for the computer. It returns a dictionary with the player's and computer's choices.

2. **`check_win(player, computer)`**: This function takes the player's and computer's choices as input and determines the winner based on the game rules. It prints the choices and the result of the game.

3. The main part of the script where the functions are called and the game is executed.

## Example

Here's an example of how the game works:

```sh
Enter a choice (rock, paper, scissors): rock
You chose rock, computer chose scissors
Rock smashes scissors! You Win!
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

