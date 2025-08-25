from flask import Flask
app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <html>
        <head>
            <title>Salam bura menim sehifemdir!</title>
                </head>
                    <body>
                <h1>Salam, menim sehifeme xos geldiniz!</h1>

    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="", port=5000)