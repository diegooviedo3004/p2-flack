from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Instancia de SocketIo
socketio = SocketIO(app, cors_allowed_origins='*')

# Usuarios alojados en memoria
usuarios = []
rooms = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('nuevo_usuario')
def nuevo_usuario(nombre):
    global usuarios
    print(usuarios)
    if nombre not in usuarios:
        usuarios.append(nombre)
        emit('login')
    else:
        emit('error','User already taken')

@socketio.on('disconnect')
def disconnect(nombre):
    print(nombre)
        
        
# Opcional
if __name__ == '__main__':
    socketio.run(app)