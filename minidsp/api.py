from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    # Здесь позже можно интегрировать HID или minidsp CLI
    return jsonify({
        "preset": "1",
        "input": "USB",
        "volume": "0 dB"
    })

@app.route("/preset", methods=["GET", "POST"])
def preset():
    if request.method == "GET":
        return jsonify({"preset": "1"})
    data = request.get_json() or {}
    p = data.get("preset")
    return jsonify({"result": f"Preset set to {p}"})

@app.route("/input", methods=["GET", "POST"])
def input_route():
    if request.method == "GET":
        return jsonify({"input": "USB"})
    data = request.get_json() or {}
    v = data.get("input")
    return jsonify({"result": f"Input set to {v}"})

@app.route("/volume", methods=["GET", "POST"])
def volume_route():
    if request.method == "GET":
        return jsonify({"volume": "0 dB"})
    data = request.get_json() or {}
    v = data.get("volume")
    return jsonify({"result": f"Volume set to {v}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
