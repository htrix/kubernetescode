from flask import Flask
import os

app = Flask(__name__)

# Lê as variáveis de ambiente criadas pelo ExternalSecret
palavra1 = os.environ.get("PALAVRA1", "default1")
palavra2 = os.environ.get("PALAVRA2", "default2")

@app.route('/')
def hello_world():
    return f'Please subscribe, like, and comment on this video !!Segredo 1: {palavra1} | Segredo 2: {palavra2}'
