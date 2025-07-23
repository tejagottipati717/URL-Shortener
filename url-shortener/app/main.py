from flask import Flask, request, jsonify, redirect
from app.models import URLStore
from app.utils import generate_short_code, is_valid_url

app = Flask(__name__)
store = URLStore()

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    url = data.get('url')

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    store.save(short_code, url)

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    record = store.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    store.increment_click(short_code)
    return redirect(record["url"])

@app.route('/api/stats/<short_code>', methods=['GET'])
def stats(short_code):
    record = store.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"]
    })
