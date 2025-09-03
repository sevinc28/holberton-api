from flask import Flask, render_template, request
import re
app = Flask(__name__)
@app.route("/register", methods=["GET", "POST"])
def qeydiyyat():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        number = request.form.get("number")

        #Asagida yoxlayaq
        if not (first_name and last_name and email and number):
            error = "Zehmet olmasa butun hisseleri doldurun"
            return render_template("register.html", error=error)
        return render_template("success.html",
                               first_name=first_name,
                               last_name=last_name,
                               email=email,
                               number=number)
    return render_template("register.html")
if __name__ == '__main__':
    app.run(debug=True)