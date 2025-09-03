from flask import Flask
app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <html>
    <head>
        <title>Salam Dunya!</title>
        <h2>Salam Dunya!</h2>
        <p>Bu menim ilk Flask web sehifemdir!</p
    </head>
    </head>
    """
    
if __name__ == "__main__":
    app.run(debug=True, host="", port = 5000)
