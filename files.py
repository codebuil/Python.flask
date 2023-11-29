from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def hello_world():
    arquivos = os.listdir(".\\")
    h=""
    for arquivo in arquivos:
        h=h+"<br><h1>"+arquivo+"<h1>"
    return h


print("\x1bc\x1b[43;30m")
app.run()
