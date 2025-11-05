from flask import Flask, render_template, redirect, jsonify
import random

app = Flask(__name__)

QUOTES = {
    "The best way to predict the future is to create it": "Peter Drucker",
    "In the middle of difficulty lies opportunity": "Albert Einstein",
    "Do what you can, with what you have, where you are": "Theodore Roosevelt",
    "Believe you can and you're halfway there": "Theodore Roosevelt",
    "Act as if what you do makes a difference. It does": "William James",
    "The only limit to our realization of tomorrow is our doubts of today.": "Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.": "Winston Churchill",
    "Happiness is not something ready-made. It comes from your own actions.": "Dalai Lama"
}

#dk
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/quote")
def quote():
    quote, author = random.choice(list(QUOTES.items()))
    return render_template('quote.html', quote=quote, author=author)

@app.route('/random-quote')
def random_quote():
    quote, author = random.choice(list(QUOTES.items()))
    return jsonify({"quote": quote, "author": author})

@app.route('/favorite')
def favorite():
    return render_template("favorite.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)