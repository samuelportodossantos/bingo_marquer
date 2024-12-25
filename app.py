from flask import Flask, render_template, request
from source.service.ball_manager import BallManager
from source.service.socket_manager import SocketManager
import asyncio
import threading
import json

ball_manager = BallManager()
socket_manager = SocketManager()


app = Flask(
    import_name="teste",
    template_folder="source/view/",
    static_folder="static/"
)

@app.route('/',  methods=["GET"])
def index():
    balls = ball_manager.get_all_balls()
    return render_template("pages/home.jinja", balls=balls)

@app.route('/form', methods=["GET"])
def form():
    return render_template('pages/form.jinja')

@app.route('/add_ball', methods=["POST"])
async def add_ball():
    ball = request.form.get('ball')
    ball_manager.new_ball(ball)
    await socket_manager.broadcast(json.dumps({"new_ball": ball}))
    return render_template('pages/form.jinja')

def run_websocket():
    asyncio.run(socket_manager.start_server())


if __name__ == "__main__" :

    ws_thread = threading.Thread(target=run_websocket, daemon=True)
    ws_thread.start()

    app.run(
        host='0.0.0.0',
        port=5000,
)

