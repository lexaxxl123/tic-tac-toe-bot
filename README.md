# ❌⭕ Tic-Tac-Toe Telegram Bot

A simple, interactive Tic-Tac-Toe game that runs inside Telegram.
I built this project to practice **Object-Oriented Programming (OOP)** in Python and to learn how to work with the **Telegram Bot API**.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Library](https://img.shields.io/badge/Library-pyTelegramBotAPI-orange)

## 🎮 Features

* **Inline Interface:** The game uses inline buttons, so you don't need to type coordinates manually.
* **Single Player Mode:** Play against a Bot (Basic AI).
* **Win Logic:** Automatically detects wins (rows, columns, diagonals) and draws.
* **Statistics:** Tracks the number of moves and announces the winner at the end.
* **Multi-user Support:** Multiple users can play their own games simultaneously without interference.

## 🛠️ Project Structure

I organized the code into separate classes to keep the logic clean:

* **`Game`**: The main controller that initializes a session for a specific chat ID.
* **`Board`**: Manages the 3x3 grid and generates the inline keyboard.
* **`Bot`**: Handles the opponent's moves (currently uses random logic for available cells).
* **`Win`**: Contains the logic to check for winning combinations or ties.
* **`Statistics`**: Tracks game progress (move counts and results).

## 🚀 How to Run

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/tic-tac-toe-bot.git](https://github.com/your-username/tic-tac-toe-bot.git)
    cd tic-tac-toe-bot
    ```

2.  **Install dependencies**
    You need the `pyTelegramBotAPI` library.
    ```bash
    pip install pyTelegramBotAPI
    ```

3.  **Configure the Token**
    * Open the Python file.
    * Replace `'YOUR_TOKEN_HERE'` with your actual API token from @BotFather.

4.  **Run the bot**
    ```bash
    python game.py
    ```

## 📸 Usage

1.  Start the bot with `/start`.
2.  The board will appear. You play as **[X]**.
3.  Click on a cell to make a move.
4.  The bot **[O]** will respond immediately.
