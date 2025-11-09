from flask import Flask, render_template, redirect, jsonify, session, url_for, request
import requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.secret_key = "your_secret_key"

#dk<
@app.route('/')
def index():
    # Fetch a random quote from the API
    response = requests.get("https://api.quotable.io/random", verify=False)

    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Could not fetch quote at this time."
        author = "Unknown"
        
    return render_template('index.html', quote=quote, author=author)

@app.route("/quote")
def quote():
    # Fetch a random quote from the API
    response = requests.get("https://api.quotable.io/random", verify=False)

    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Could not fetch quote at this time."
        author = "Unknown"
    return render_template('quote.html', quote=quote, author=author)

@app.route('/random-quote')
def random_quote():
    # Fetch a random quote from the API
    response = requests.get("https://api.quotable.io/random", verify=False)

    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Could not fetch quote at this time."
        author = "Unknown"
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