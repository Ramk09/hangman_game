# 🎮 Hangman Game

A simple and interactive **Hangman Game** built using **Python and Flask**. Players try to guess a randomly selected word one letter at a time before running out of lives.

## ✨ Features

- 🎯 Three difficulty levels:
  - Easy
  - Medium
  - Hard
- 🔤 Random word selection
- ❤️ 5 lives per game
- 📝 Tracks previously guessed letters
- ✅ Detects correct and incorrect guesses
- 🎉 Win and game-over messages
- 💀 ASCII Hangman stages
- 🔄 New Game option
- 🌐 Flask-based web interface
- 🔐 Flask session-based game state

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML/CSS**
- **Jinja2**
- **Python Sessions**

## 📂 Project Structure

```text
Hangman-Game/
│
├── app.py
├── words.py
├── hangman_stages.py
├── templates/
│   └── index.html
├── static/
│   └── ...
└── README.md
```

### 📄 File Description

| File | Description |
|---|---|
| `app.py` | Main Flask application and game logic |
| `words.py` | Contains words categorized by difficulty |
| `hangman_stages.py` | Contains ASCII Hangman drawings |
| `templates/index.html` | Web interface for the game |
| `static/` | CSS and other frontend files |
| `README.md` | Project documentation |

The application imports the word list and Hangman stages into the Flask app.

## 🎚️ Difficulty Levels

### 🟢 Easy
Contains simple words such as:

```text
ram
cat
dog
sun
moon
tree
book
fish
milk
king
```

### 🟡 Medium
Contains words such as:

```text
python
computer
student
program
developer
machine
project
hangman
keyboard
internet
```

### 🔴 Hard
Contains more challenging words such as:

```text
artificial
intelligence
algorithm
programming
development
technology
cybersecurity
visualization
environment
architecture
```

The words are organized into `easy`, `medium`, and `hard` categories.

## 🎮 How to Play

1. Start the application.
2. Select a difficulty level.
3. A random word will be selected.
4. Enter one letter at a time.
5. Correct guesses reveal the letter.
6. Incorrect guesses reduce your lives.
7. Guess the complete word before your lives reach zero.
8. Start a new game whenever you want.

The application starts a new game with the selected difficulty and gives the player **5 lives**.

## ⚙️ Game Logic

The game validates user input to ensure that:

- A letter is entered.
- Only one character is entered.
- The character is alphabetic.
- The same letter isn't guessed repeatedly.

Correct guesses are added to the guessed-letter list, while incorrect guesses decrease the player's lives.

The game ends when either:

- 🎉 All letters in the word have been guessed, or
- 💀 The player's lives reach zero.

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hangman-game.git
```

### 2. Open the Project

```bash
cd hangman-game
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Go to:

```text
http://127.0.0.1:5000/
```

## 📸 Game Interface

Add screenshots of your game here after uploading them to your repository.

```markdown
![Hangman Game](screenshots/game.png)
```

## 🔮 Future Improvements

- 🔊 Add sound effects
- 🏆 Add a scoring system
- 📊 Add a leaderboard
- 🎨 Improve UI/UX
- 📱 Make the interface responsive
- 🗃️ Add a larger word database
- 👤 Add user accounts
- 📈 Track player statistics
- 🌍 Add multiple languages

## 👨‍💻 Author

**Kurra Venkata Siva Rama Krishna**

B.Tech — Artificial Intelligence & Machine Learning

---

⭐ If you like this project, consider giving the repository a **star**!
