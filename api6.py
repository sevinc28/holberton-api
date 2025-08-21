from flask import Flask
app = Flask(__name__)
@app.route('/')
def ana_sehife():
    return """
    <html>
        <head>
            <title>Salam,Cantalar.alem1 sehifesine xos geldiniz!"</title>
                </head>
                    <body>
                <h1>Salam, Cantalar.alem1 sehifesine xos geldiniz!</h1>
                <p>Sifaris ucun: +994 55 237 95 43</p>
        <h2>Burada zovqunuze uygun cantalar movcuddur</h2>
        <strong>Cantalar</strong> (bags) gundelik ve ziyafet geyimlerin tamamlayici hisseleridir ve onlari daha gozel ve funksional edir<br>
        <ul>
            <li>Gorunusu gozel gosterir</li>
            <li>Geyimlerin tamamlayici hisseleridir</li>
            <li>Gerqli zovqunuze uygun cantalar movcuddur</li>
            <li>Ziyafet ve gundelik geyimleri tamamlayir</li>
        </ul>
        <p>Bizim xidmetlerimiz:</p>
            <p><a href="/xidmetler">Xidmetlerimiz</p>
        </body>
    </html>
    """
@app.route("/xidmetler")
def xidmetler_sehifesi():
    return """
    <html>
        <head>
            <title>Xidmetlerimiz</title>
                </head>
                    <body>
                <h2>Xidmetlerimiz</h2>
            <p>Mekteb cantalari</p>
        <p>Gundelik cantalar</p>
    <p>Qadin canalari</p>
<p>Ve daha coxu...</p>
    <p>Daha etrafli melumat ucun: +994 55 237 95 43</p>
        <p><a href="/">Ana sehifeye qayit</a></p>
    </body>
</html>
    """
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)