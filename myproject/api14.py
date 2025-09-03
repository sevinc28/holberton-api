from flask import Flask
app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <html>
        <head><title>Lovebjuu.az</title></head>
            <body>
                <h2>Lovebjuu sehifesine xos gelmisiniz</h2>
            <hr></hr>
        <p>Burada zovqunuze uygun aksesuarlar movcuddur</p>
            <h3><strong>Aksesuarlar </strong>geyimlerin tamamlayici hisseleridir</h3>
                <ul>
                    <li>Ziyafet geyimleri ucun aksesuarlar</li>
                    <li>Gundelik geyimler ucun aksesuarlar</li>
                    <li>Ferqli aksesuarlar</li>
                </ul>
            <h3>Bizim aksesuarlar</h3>
        <ol>
            <li>Qadin aksesuarlari</li>
            <li>Kisi aksesuarlar</li>
            <li>Usaq aksesuarlar</li>
        </ol>
    <h3>Etrafli melumat almaq ucun: +994 237 95 43</h3>
        </body>
        </html>
    """
if __name__ == '__main__':
    app.run(debug=True)