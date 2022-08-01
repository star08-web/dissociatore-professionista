from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return 'lol'


def run():
    app.run(host='0.0.0.0', port=8080)


def stayalive():
    t = Thread(target=run)
    t.start()
