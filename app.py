#!/usr/bin/env python3
"""
A simple Flask web server that serves a mouse-tracking interactive page.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page with mouse tracking."""
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting server on http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)

