from flask import Flask, jsonify

app = Flask(__name__)

BOT_STATUS = "parado"

@app.route("/")
def home():
    return f"""
    <h1>🤖 Trading Bot</h1>
    <p>Status: <b>{BOT_STATUS}</b></p>
    <a href='/start'>▶ Iniciar</a><br><br>
    <a href='/stop'>⏹ Parar</a>
    """

@app.route("/start")
def start_bot():
    global BOT_STATUS
    BOT_STATUS = "rodando"
    return jsonify({"status": BOT_STATUS})

@app.route("/stop")
def stop_bot():
    global BOT_STATUS
    BOT_STATUS = "parado"
    return jsonify({"status": BOT_STATUS})

