from flask import Flask
app = Flask(__name__)
@app.route('/')
def ana_sehife():
    return """
    <h1> Salam Xos gelmisiniz!>
    <p>
    <a href="/rengler">Kataloq sehifesine kecid et</a>
    <a href=Menyu</a>
    </p>
    """
@app.route("/rengler")
def rengli_sehife():
    return """
    <h1 style="color:purple;">Welcome!</h1>
    <hr>
    """
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)