## (eye emojis)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", id='7fMu62nb6fotKFfWhARUi4')

if __name__ == '__main__':
    app.run()
