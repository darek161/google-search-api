from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return jsonify({
        "status": "ok",
        "query": query,
        "message": "Działa! To jest wersja testowa bez Google API."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
