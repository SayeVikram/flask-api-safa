# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:57:35 2022

@author: ts_ka
"""
from webscraper import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return scrape_google("Education");


if __name__ == "__main":
    app.run(host='0.0.0.0', port=5000)

