from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
CX = os.environ.get("CX")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Google API error"}), response.status_code

    results = response.json().get("items", [])
    return jsonify([
        {
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        }
        for item in results
    ])

app.run(host='0.0.0.0', port=8080)