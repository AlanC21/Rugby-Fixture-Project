from flask import Flask

app = Flask(__name__)

from api import response

@app.route('/')
def getApi():
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=4000)