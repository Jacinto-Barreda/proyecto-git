from asyncio import run_coroutine_threadsafe
from curses import flash
from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
     return "hello world"

@app.route("/")
def index():
     return "hello farlen"

@app.route("/")
def index():
     return "hello gato"
