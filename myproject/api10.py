from flask import Flask
app = Flask(__name__)
@app.route('/')
def sehife():
    return """
    <html>
        <head>
            <h1>Heyvanlar haqqinda melumat sehifesine xos geldiniz!</h1>
            <p>Burada heyvanlar haqqinda melumatlar movcuddur</p>
            <p>Bu gun balina haqqinda melumat verilecek</p>
            <ul>
                <li>Balinalar su heyvanlaridir</li>
                <li>Balinalar sutle beslenen heyvanlardandir</li>
                <li>Balinalar insanlarla cox mehribandir</li>
                <li>Balinalar okeanlarda yasayir</li>
            </ul>
        <img src="
        </head>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host="", port = 5000)