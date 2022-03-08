from flask import Flask, render_template
import json
app = Flask(__name__)
from random import randrange
@app.route("/member")
def member():
    file = open("templates/name.json").read()
    dic = json.loads(file)
    return render_template("name.html", user=dic['users'][randrange(len(dic["users"]))])


if __name__ == "__main__":
    app.run()
