from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def ask():
    return "<h1>Guess a number between 0 and 9.</h1>" \
           "<img src='https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif?cid=790b761137b8a15ea33e74b5b999cc49815ee16a140e4b1b&rid=giphy.gif&ct=g' width=450px>"


@app.route('/<int:user_input>')
def check_number(user_input):
    number = random.randint(0, 9)
    if user_input == number:
        return f"<h1 style='color: green'>Correct Guess.</h1>"
    elif user_input < number - 2:
        return f"<h1 style='color: red'>Too Low, Try Again!</h1>"
    elif user_input > number + 2:
        return f"<h1 style='color: red'>Too High, Try Again!</h1>"
    elif user_input < number:
        return f"<h1 style='color: red'>Low but near, Try Again!</h1>"
    elif user_input > number:
        return f"<h1 style='color: red'>High but near, Try Again!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
