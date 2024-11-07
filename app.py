import requests
from urllib.parse import urlencode
import re
from datetime import datetime

from flask import Flask
app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()


@app.route("/<word>")
def home(word):
    base_url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}"
    params = {
        "key": os.getenv("API_KEY")
    }

    url = f"{base_url}?{urlencode(params)}"
    response = requests.get(url)


    shortdef = response.json()[0]['shortdef']

    rtn = f"<p>The definition of <strong>{word}</strong> is:\n\n<p>" + "".join(f'<p>{i+1}: {definition}<p>' for i, definition in enumerate(shortdef))
    
    
    return rtn


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
