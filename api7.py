from flask import Flask
app = Flask(__name__)

@app.route('/')
def love_page():
    return """
    <html>
        <head>
            <title>Salam Lovebjuu sehifesine xos geldiniz!</title>
            <h2>Salam, Lovebjuu sehifesine xos geldiniz!</h2>
            <ul>
                <p>Kataloq</p>
                <p>Mehsullar</p>>
                <p>Elaqe</p>
                <p>Haqqimizda</p>
            </ul>
            <p>Mehsullar haqqinda daha etrafli melumat ucun: +994 55 237 95 43</p>
        </head>
    </html>
        """

@app.route("/rengler")
def rengli_sehife():
    return """
    <html>
        <head>
            <title>Rengler</title>
                <h2>Salam, Lovebjuu sehifesine xos geldiniz!</h2>
                    <p>Burada mehsullar haqqinda melumatlar var.</p>
                        <p>Gumus sepler, uzukler, destler, boyunbaglar ve daha coxu...</p>
                            <p>Mehsullar haqqinda daha etrafli melumat ucun: +994 55 237 95 43</p>
                        <p><a href="/">Ana sehifeye qayit</a></p>
                    </head>
                </html>
            """

@app.route("/mehsullar")
def mehsullar_sehifesi():
    return """
    <html>
    <head>
        <title>Mehsullar</title>
            <h2>Populyar Mehsullar</h2>
        <ul>
            <li>:ring: Gümüş üzük</li>
            <li>:gift: Hədiyyə dəsti</li>
        </ul>
    <p>Ətrafli məlumat üçün: +994 55 237 95 43</p>
    <p><a href="/">Ana səhifəyə qayit</a></p>
    </head>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host="")