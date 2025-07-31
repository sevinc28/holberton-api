from flask import Flask
app = Flask(__name__)
@app.route('/')
def ana_sehife():
    return """
   <h1>Salam!Lovebjuu sehifesine xos geldiniz!</h1>
   <p>
   <a href="/rengler">Kataloq sehifesine kecid et</a>
   </p>
   """
@app.route("/rengler")
def rengli_sehife():
    return """
    <h2 style="color:red;">Welcome!</h2>
    <p style="color:red;">This is the Lovebjuu catalog"</p>
    <p style="color:purple;">Silvers</p>
    <p style="color:red;">Bags</p>
    <hr>
    """
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)