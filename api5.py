from flask import Flask
app = Flask(__name__)

@app.route('/')
def sehife():
    return """
    <html>
    <head><title>Salam Lovebjuu sehifesine xos geldiniz</title></head>
    <body>
        <h1>Salam Lovebjuu sehifesine xos gelmisiniz!</h1>
        <p>
        <h3>Sifaris ucun: +994 55 237 95 43</h3>
        </p>
        <h2>Burada zovqunuze uygun aksesuarlar movcuddur</h2>
        <strong> Aksesuarlar</strong> (accessories) geyimlerin tamamlayici hisseleridir ve onlari daha gozel ve funksional edin<br>
        <ul>
            <li>Gorunusu gozel gosterir</li>
            <li>Geyimlerin tamamlayici hisseleridir</li>
            <li>Gerqli zovqunuze uygun aksesuarlar movcuddur</li>
            <li>Ziyafet ve gundelik geyimleri tamamlayir</li>
        </ul>
        </body>
        </html>
        """
if __name__ == '__main__':
    app.run(debug=True, host="")