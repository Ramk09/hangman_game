from flask import Flask, render_template, request, session, redirect, url_for
import random

from words import words
from hangman_stages import stages


app = Flask(__name__)

# Required for Flask sessions
app.secret_key = "hangman-secret-key"


@app.route("/", methods=["GET", "POST"])
def index():

    # Start a new game if there is no active game
    if "word" not in session:
        start_new_game("easy")

    message = session.get("message", "")
    message_type = session.get("message_type", "")

    if request.method == "POST":

        action = request.form.get("action")

        # -------------------------
        # NEW GAME
        # -------------------------
        if action == "new_game":

            difficulty = request.form.get("difficulty", "easy")

            start_new_game(difficulty)

            return redirect(url_for("index"))

        # -------------------------
        # GUESS LETTER
        # -------------------------
        if action == "guess":

            guessed_letter = request.form.get(
                "letter", ""
            ).lower().strip()

            word = session["word"]
            guessed_letters = session["guessed_letters"]

            # Check empty input
            if not guessed_letter:

                session["message"] = "Please enter a letter."
                session["message_type"] = "error"

            # Check only one character
            elif len(guessed_letter) != 1 or not guessed_letter.isalpha():

                session["message"] = "Please enter one valid letter."
                session["message_type"] = "error"

            # Check repeated letter
            elif guessed_letter in guessed_letters:

                session["message"] = (
                    f"You already guessed '{guessed_letter.upper()}'."
                )
                session["message_type"] = "error"

            else:

                guessed_letters.append(guessed_letter)

                # Correct guess
                if guessed_letter in word:

                    session["message"] = (
                        f"Great! '{guessed_letter.upper()}' is correct! 🎉"
                    )
                    session["message_type"] = "success"

                # Wrong guess
                else:

                    session["lives"] -= 1

                    session["message"] = (
                        f"'{guessed_letter.upper()}' is not in the word."
                    )
                    session["message_type"] = "error"

                # Check WIN
                if all(
                    letter in guessed_letters
                    for letter in word
                ):

                    session["game_over"] = True
                    session["won"] = True

                    session["message"] = (
                        f"🎉 You Won! The word was '{word.upper()}'."
                    )

                    session["message_type"] = "success"

                # Check LOSE
                elif session["lives"] <= 0:

                    session["game_over"] = True
                    session["won"] = False

                    session["message"] = (
                        f"💀 Game Over! The word was '{word.upper()}'."
                    )

                    session["message_type"] = "error"

                session.modified = True

            return redirect(url_for("index"))

    # Create displayed word
    displayed_word = []

    for letter in session["word"]:

        if letter in session["guessed_letters"]:
            displayed_word.append(letter.upper())
        else:
            displayed_word.append("_")

    # Get hangman stage
    lives = session["lives"]

    stage_index = 5 - lives

    if stage_index < 0:
        stage_index = 0

    if stage_index > 5:
        stage_index = 5

    current_stage = stages[stage_index]

    return render_template(
        "index.html",
        displayed_word=" ".join(displayed_word),
        guessed_letters=session["guessed_letters"],
        lives=session["lives"],
        difficulty=session["difficulty"],
        stage=current_stage,
        message=message,
        message_type=message_type,
        game_over=session["game_over"],
        won=session["won"]
    )


def start_new_game(difficulty):

    # Select random word
    selected_word = random.choice(words[difficulty]).lower()

    session["word"] = selected_word
    session["guessed_letters"] = []
    session["lives"] = 5
    session["difficulty"] = difficulty

    session["game_over"] = False
    session["won"] = False

    session["message"] = "Guess a letter to start!"
    session["message_type"] = "info"


if __name__ == "__main__":
    app.run(debug=True)