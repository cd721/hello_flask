from dotenv import load_dotenv
import os
import requests
from urllib.parse import urlencode
import re
from datetime import datetime

from flask import Flask, jsonify, render_template, make_response
app = Flask(__name__)


load_dotenv()


@app.route("/favicon.ico")
def favicon():
    return ""


@app.route("/<word>")
def word(word):
    if (word.strip()) == "":
        return make_response(render_template("bad_input.html"), 400)
    base_url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}"
    params = {
        "key": os.getenv("API_KEY")
    }

    url = f"{base_url}?{urlencode(params)}"
    response = requests.get(url)

   
    if response.json() == []:
        print("User entered an invalid word. The Dictionary API did not provide suggestions.")
        return make_response(render_template("invalid_word.html", suggestions=[]), 404)
    elif (isinstance(response.json(), list)) and (isinstance(response.json()[0], str)):
        suggestions = response.json()
        print("User entered an invalid word. The Dictionary API did not provide suggestions.")
        return make_response(render_template("invalid_word.html", suggestions=suggestions), 302)

    shortdef = response.json()[0]['shortdef']

    return make_response(render_template("index.html", word=word, definitions=shortdef),200)


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/")
def home():
    json = jsonify(data="Hello, World", status=200)

    return render_template("index.html", text=json)


if __name__ == '__main__':
    app.run(debug=True)
