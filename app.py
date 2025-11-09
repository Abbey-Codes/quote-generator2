from flask import Flask, render_template, redirect, jsonify, session, url_for, request
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

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

#dk<
@app.route('/')
def index():
    quote, author = random.choice(list(QUOTES.items()))
    return render_template('index.html', quote=quote, author=author)

@app.route("/quote")
def quote():
    quote, author = random.choice(list(QUOTES.items()))
    return render_template('quote.html', quote=quote, author=author)

@app.route('/random-quote')
def random_quote():
    quote, author = random.choice(list(QUOTES.items()))
    return jsonify({"quote": quote, "author": author})

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    quote = request.form['quote']
    author = request.form['author']

    # initialise session if empty
    if 'favorites' not in session:
        session['favorites'] = []

    favorite = {'quote': quote, 'author': author}
    if favorite not in session['favorites']:
        session['favorites'].append(favorite)
        session.modified = True


    return redirect(url_for('quote'))

@app.route('/remove_favorite', methods=['POST'])
def remove_favorite():
    quote = request.form['quote']
    author = request.form['author']

    # remove the item from session favorites
    if 'favorites' in session:
        for favorite in session['favorites']:
            if favorite['quote'] == quote and favorite['author'] == author:
                session['favorites'].remove(favorite)
                session.modified = True
                break # stop after removing the matching quote
    return redirect(url_for('favorite'))

@app.route('/favorite')
def favorite():
    favorites = session.get('favorites', [])
    return render_template("favorite.html", favorites=favorites)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)