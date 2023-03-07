# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def enigma(methods=['get']):
    return "Hello, World!"


@app.route("/enigma")
def enigma(methods=['post']):
    return "Hello, World!"

@app.route("/deenigma")
def de_enigma(methods=['post']):
    return "Hello, World!"

if __name__ == '__main__':


    app.run(debug= False)
