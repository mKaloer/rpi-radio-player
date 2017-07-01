from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')


@app.route("/discover")
def discover():
    return render_template('discover.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
