from flask import Flask
app = Flask(__name__)
@app.route('/')
def ana_səhifə():
    return """
    <head>
     <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="background-color:#f5f7fa; font-family: 'Poppins', sans-serif; margin: 40px;">
      <h1 style="color:#2c3e50; font-weight: 700;">Salam! Xoş gəldiniz!</h1>
      <p style="color:#34495e; font-size: 18px;">
        Bu Aysun Teymurzadənin şəxsi veb saytıdır.
      </p>
      <p>
        <a href="/xidmetler" style="color:#2980b9; text-decoration:none; font-weight:600; font-size: 20px;"
           onmouseover="this.style.color='#1ABC9C';"
           onmouseout="this.style.color='#2980B9';">
          Xidmətlərimiz :arrow_down:
        </a>
      </p>
      <hr style="border: 1px solid #ECF0F1; margin-top: 40px;">
    </body>
    """
@app.route("/xidmetler")
def xidmetler_sehifesi():
    return """
    <body style="background-color: #F5F7FA; font-family: 'Poppins', sans-serif; margin: 40px;">
      <h2 style="color:#2c3e50;">:sparkles: Gəlin, xidmətlərimizlə tanış olaq:</h2>
      <p style="color:#34495e; font-size: 18px;">:blue_book: Elmi işlərinizin yazılması :white_check_mark:</p>
      <p style="color:#34495e; font-size: 18px;">:art: Poster dizaynı</p>
      <p style="background-color:#ecf0f1; color:#2c3e50; padding: 10px; border-radius: 5px;">
        :rocket: Və daha çoxu...
      </p>
      <hr style="border: 1px solid #DFE6E9;">
      <p style="background-color:#ffeaa7; color:#2d3436; padding: 12px; border-radius: 5px;">
        :telephone_receiver: Daha ətraflı məlumat üçün: <strong>+994516422855</strong>
      </p>
      <p>
        <a href="/" style="color:#0984e3; text-decoration:none; font-weight: bold; font-size:16px;">
          :arrow_left: Geri dön
        </a>
      </p>
    </body>
    """
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)