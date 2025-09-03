from flask import Flask
app = Flask(__name__)

@app.route('/')
def sehife():
    return """
    <html>
        <head><title>Lovebjuu.az</title></head>
            <body>
                <h1>Lovebjuu sehifesine xos gelmisiniz!</h1>
                    <hr></hr>
                <h2>Burada zovqunuze uygun aksesuarlar movcuddur</h2>
             <strong> Aksesuarlar</strong> (accessories) geyimlerin tamamlayici hisseleridir<br>
        <ul>
            <li>Gorunusu gozel gosterir</li>
            <li>Geyimlerin tamamlayici hisseleridir</li>
            <li>Ferqli zovqunuze uygun aksesuarlar movcuddur</li>
            <li>Ziyafet ve gundelik geyimleri tamamlayir</li> 
        </ul>
        <img src="https://www.sochic.com/blog/wp-content/uploads/2024/06/Deniz-Temali-Takilar-Plaj-Sikligini-Yansitan-Aksesuarlar-scaled.jpg"
            style="width:300px;
                heigth:auto;" alt="Sekil"; float: left;">
                    <h3>Bizim aksesuarlarimiz</h3>
            <ol>
                <li>Qadin aksesuarlari</li>
                <li>Kisi aksesuarlari</li>
                <li>Usaq aksesuarlari</li>
            </ol>

        <h3>Etrafli melumat ucun: +994 237 95 43</h3>

    </body>
    </html>
        """ssss
if __name__ == '__main__':
    app.run(debug=True, host="")