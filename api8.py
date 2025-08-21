from flask import Flask
app = Flask(__name__)

@app.route('/')
def fruit():
    return """
    <html>
        <head>
            <h1>Salam, Lovebjuu sehifesine xos geldiniz!</h1>
            <p>Sifaris ucun: +994 55 237 95 43</p>
            <h2>Burada zovqunuze uygun aksesuarlar movcuddur</h2>
            <strong>Lovebjuu</strong> (accesories) gundelik ve ziyafet geyimlerin tamamlayici hisseleridir ve onlari daha gozel ve funksional edir<br>
            <ul>
                <li>Gorunusu gozel gosterir</li>
                <li>Geyimlerin tamamlayici hisseleridir</li>
                <li>Gerqli zovqunuze uygun aksesuarlar movcuddur</li>
                <li>Ziyafet ve gundelik geyimleri tamamlayir</li>
            </ul>
            <p>Bizim xidmetlerimiz:</p>
            <p><a href="/xidmetler">Xidmetlerimiz</a></p>
        </head>
        </html>
    """
if __name__ == "__main__":
    app.run(debug=True, host='')