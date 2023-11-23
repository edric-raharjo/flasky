from flask import url_for,Flask, render_template, request, jsonify, redirect
import random
import logging

app = Flask(__name__, template_folder="templates", static_folder="static")
# app.config["DEBUG"] = True  

def generate_random(name = None):
    if name:
        name = name.title()
        choices = [
            f"No {name}, That's Modalism",
            f"No {name}, That's Subordinationism",
            f"No {name}, That's Adoptionism",
            f"No {name}, That's Arianism",
            f"No {name}, That's Sabellianism",
            f"No {name}, That's Tritheism",
            f"No {name}, That's Nestorianism",
            f"No {name}, That's Eutychianism",
            f"No {name}, That's Monophysitism",
            f"No {name}, That's Docetism"
        ]    

    else:
        choices = [
            "No Patrick, That's Modalism",
            "No Patrick, That's Subordinationism",
            "No Patrick, That's Adoptionism",
            "No Patrick, That's Arianism",
            "No Patrick, That's Sabellianism",
            "No Patrick, That's Tritheism",
            "No Patrick, That's Nestorianism",
            "No Patrick, That's Eutychianism",
            "No Patrick, That's Monophysitism",
            "No Patrick, That's Docetism"
        ]

    return random.choice(choices)

@app.route("/<name>")
def random_heresy(name = None):
    return render_template("kerang.html", kataAjaib = f"{generate_random((name))}")

@app.route('/success/<name>')
def success(name):
    return render_template("kerang.html", kataAjaib = f"{generate_random((name))}")

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get("nm")
        return redirect(url_for('success',name = user))
    
@app.route("/form/")
def form():
    return render_template("index.html")
    