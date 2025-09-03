from flask import Flask
app = Flask(__name__)

@app.route('/')
def sehife():
    return """
        <html>
            <head><title>Hava Proqnozu</title></head>
                <body>
            <h2>Bu gunun Hava proqnozu</h2>
        <ul>
            <li>Hava 30 derece istidir</li>
            <li>Hava guneslidir</li>
            <li>Esasen hava yagmursuz kececek</li>
        </ul>
    <img src="https://qafqazinfo.az/uploads/1755696267/hava.jpg"
    style="width:300px;heigth:auto;" alt="Sekil">
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)