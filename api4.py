from flask import Flask
app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <html>
    <head><title>Salam burada kod yazacayiq</title></head>
    <body>
        <h1>Salam Xos gelmisiniz!</h1>
        <h2>Burda API haqqinda melumat oyreneceyik</h2>
        <p>
        <strong>API</strong> (Application Programming Interface) proqramlar arasinda elaqe qurmaq ucun istifade olunan bir interfeysdir.<br>
        API-lar, proqramlarin bir-biri ile danismaq, melumat paylasmaq ve funksiyalari istifade etmek ucun standart yollar teqdim edir.<br>
        </strong>
        </p>
        <ul>
            <li>API-lar, proqramlarin bir-biri ile danismaq ucun standart yollar teqdim edir.</li>
            <li>h1 - Bu en boyuk baasliqdir</li>
            <li>h2 - Bu kicik basliqdir</li>
            <li>p - Bu bir paraqrafdir </li>
            <li>mark - <mark> Sari fonlu yazi yazilir </mark><li>
            <li>small - kicik olculu yazidir</li>
            <li>del - <del> ustunden xett cekir.</del></li>
            <li>ins - <ins> altindan xett cekir.</ins></li>
            <li>br - yeni serte kecir</li>
            <li>hr - horizontal xett cekir</li>
        </ul>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True, host="")