from flask import Flask
app = Flask(__name__)
@app.route('/')
def sehife():
    return """
    <html>
    <head><title>Cantalar.alem1</title></head>
    <h1><em>Cantalar.alem1 sehifesine xos gelmisiniz!</em></h1>

    <hr></hr>
    <p>Etrafli melumat almaq ucun kecidden istifade edin</p>
    <a href="/xidmetler">Kataloq sehifesine kecid et</a>
    """
@app.route("/xidmetler")
def xidmetler_sehife():
    return """
<h2>Xidmetlerimiz</h2>
    <ul>
    <li>Mekteb cantalari</li>
    <li>Gundelik cantalar</li>
    <li>Ziyafet cantalar</li>
    </ul>
    """


if __name__ == '__main__':
    app.run(debug=True)