from flask import Flask, render_template, redirect

app = Flask(__name__)

#dk
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/quote")
def quote():
    return render_template('quote.html')

@app.route('/favorite')
def favorite():
    return render_template("favorite.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)