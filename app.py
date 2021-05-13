from flask import Flask, render_template_string
from flask.templating import render_template
from flask_socketio import SocketIO, send
from werkzeug import debug

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def listen_message(msg):
    print("Message: " + msg)
    send(msg, broadcast = True)


if __name__ == '__main__':
    socketio.run(app, debug = True)