from flask import Flask, render_template, request

app = Flask(__name__)

# GloBal Variable (전역변수)
student_list = [
    "오동건",
    "지민수",
    "이유겸",
    "김태민",
    "정예림",
    "장세진",
    "장인환",
]

# 기능


@app.route("/")
def home():
    return render_template("index.html", studnets=student_list)


@app.route("/add")
def add():

    r_txt = request.args.get("s_name", type=str)

    student_list.append(r_txt)

    return render_template("index.html", studnets=student_list)


@app.route("/remove")
def remove():

    r_txt = request.args.get("s_name", type=str)

    student_list.remove(r_txt)

    return render_template("index.html", studnets=student_list)


app.run(debug=True)
