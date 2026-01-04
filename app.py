from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

BOT_STATUS = "parado"
LAST_SIGNAL = "aguardando"
LAST_PRICE = 0.0
LAST_UPDATE = ""

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url, timeout=10).json()
    return float(data["price"])

def analyze(price):
    # análise simples (placeholder)
    if price % 2 == 0:
        return "COMPRA"
    else:
        return "AGUARDAR"

@app.route("/")
def home():
    return f"""
    <h1>🤖 Trading Bot (Dados Reais)</h1>
    <p>Status: <b>{BOT_STATUS}</b></p>
    <p>Preço BTC: <b>{LAST_PRICE}</b></p>
    <p>Sinal: <b>{LAST_SIGNAL}</b></p>
    <p>Atualizado em: {LAST_UPDATE}</p>
    <a href='/start'>▶ Iniciar</a><br><br>
    <a href='/stop'>⏹ Parar</a>
    """

@app.route("/start")
def start_bot():
    global BOT_STATUS, LAST_PRICE, LAST_SIGNAL, LAST_UPDATE
    BOT_STATUS = "rodando"

    price = get_price()
    LAST_PRICE = price
    LAST_SIGNAL = analyze(price)
    LAST_UPDATE = time.strftime("%H:%M:%S")

    return jsonify({
        "status": BOT_STATUS,
        "price": LAST_PRICE,
        "signal": LAST_SIGNAL
    })

@app.route("/stop")
def stop_bot():
    global BOT_STATUS
    BOT_STATUS = "parado"
    return jsonify({"status": BOT_STATUS})

if __name__ == "__main__":
    app.run()
