import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "message": "Hello from Flask inside Docker 🚀",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/info")
def info():
    return jsonify({
        "app": "Docker Flask Demo",
        "version": "1.0.0",
        "author": "Mostafa"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
