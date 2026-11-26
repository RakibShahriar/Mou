from flask import Flask, render_template, request, redirect, url_for, session

from flask import request

app = Flask(__name__)

app.secret_key = "mou_secret_key"

EMAIL = "sandm@gmail.com"
PASSWORD = "samirlovesmou"

PAGE12_PASSWORD = "yes"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == EMAIL and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("page1"))

        else:
            return render_template(
                "login.html",
                error="Incorrect Gmail or password."
            )

    return render_template("login.html")


@app.route("/page1")
def page1():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template("page1.html")
@app.route("/page2")
def page2():

    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template("page2.html")

@app.route("/page3")
def page3():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page3.html")

@app.route("/page4")
def page4():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page4.html")

@app.route("/page5")
def page5():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page5.html")


@app.route("/page6")
def page6():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page6.html")
@app.route("/page7")
def page7():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page7.html")

@app.route("/page8")
def page8():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page8.html")

@app.route("/page9")
def page9():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page9.html")

@app.route("/page10")
def page10():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page10.html")

@app.route("/page11")
def page11():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("page11.html")

@app.route("/page12", methods=["GET", "POST"])
def page12():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        password = request.form.get("password", "")

        if password == PAGE12_PASSWORD:
            session["page12_unlocked"] = True
            return redirect(url_for("page13"))

        return render_template(
            "page12.html",
            error="Incorrect password. Try again ❤️"
        )

    return render_template("page12.html")

@app.route("/page13")
def page13():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if not session.get("page12_unlocked"):
        return redirect(url_for("page12"))

    return render_template("page13.html")

@app.route("/page15")
def page15():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    return render_template("page15.html")

if __name__ == "__main__":
    app.run(debug=True)