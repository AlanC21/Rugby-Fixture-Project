from flask import Flask, render_template

app = Flask(__name__)

from api import response

@app.route('/')
def getApi():
    return render_template('index.html', data=response.json())

def pageNoFound(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pageNoFound)
    app.run(debug=True, port=4000)