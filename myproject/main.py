from flask import Flask

app = Flask (__name__)

@app.route('/')

def start():
    return '<h2>I Love LOVEBJUU</h2>'
    