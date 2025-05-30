"""
app.py

A simple Flask application for the IELTS Speaking Test platform demo.
- / route: Returns a greeting message.
- /welcome route: Accepts a test-taker's name and returns a personalized JSON message.

To run:
    $ export FLASK_APP=app.py
    $ flask run
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    """
    Root route.
    Returns a simple greeting as plain text.
    """
    return "Hello, Test Taker!", 200

@app.route("/welcome")
def welcome():
    """
    Welcome route.
    Accepts a 'name' query parameter and returns a personalized welcome message as JSON.
    Handles missing name gracefully.
    """
    name = request.args.get("name", "").strip()
    if not name:
        # Handle missing or empty name parameter
        return jsonify({"error": "Missing 'name' query parameter."}), 400

    message = f"Welcome to the IELTS Speaking Test, {name}!"
    return jsonify({"message": message}), 200

if __name__ == "__main__":
    app.run(debug=True)