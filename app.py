import json
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (in a real application, this would be replaced with a database)
guestbook_entries = []

# start page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entries', methods=['GET'])
def get_entries():
    return jsonify(guestbook_entries)

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    guestbook_entries.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
