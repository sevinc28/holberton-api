from flask import Flask
app = Flask(__name__)

@app.route('/')
def love_page():   
    return """
    <html>
        <head>
            <title>Lovebjuu.az</title>
           
                <h2>Lovebjuu sehifesine xos geldiniz!</h2>
                    <p>Burada mehsullar haqqinda melumatlar var.</p>
                   
                <p>Gumus sepler, uzukler, destler, boyunbaglar ve daha coxu...</p>
                <p>Mehsullar haqqinda daha etrafli melumat ucun: +994 55 237 95 43</p>
                <a href="/mehsullar"</a>
                <p><a href="/">Ana sehifeye qayit</a></p> 
                        
    </head>
    </html>
    """

@app.route("/mehsullar")
def mehsullar_sehifesi():
    return """
            <h2>Populyar Mehsullar</h2>
        <ul>
            <li>Gümüş üzük</li>
            <li>Hədiyyə dəsti</li>
        </ul>
    <p><a href="/">Ana səhifəyə qayit</a></p>
    """

app.route("/elaqe")
def elaqe_sehifesi():
    return """
    <h2>Etrafli melumat almaq ucun: +994 237 95 43</h2>
    """
    
if __name__ == '__main__':
    app.run(debug=True, host="")