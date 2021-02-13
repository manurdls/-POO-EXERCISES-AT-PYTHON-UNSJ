from flask import Flask

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Mi primer aplicación Flask!'

if __name__ == '__main__':
    app.run()