from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index_copy():
    return render_template('index_copy.html')


if __name__ == '__main__':
    app.run()
