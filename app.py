import json
import os
from datetime import datetime, timezone
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'alpha.json')


def load_entries():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, encoding='utf-8') as file:
        return json.load(file)


guestbook_entries = load_entries()

# start page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entries', methods=['GET'])
def get_entries():
    return jsonify(guestbook_entries)

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json(silent=True) or {}
    entry = {
        'name': data.get('name', '').strip(),
        'last_name': data.get('last_name', '').strip(),
        'message': data.get('message', '').strip(),
        'email': data.get('email', '').strip(),
        'timestamp': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }
    guestbook_entries.append(entry)
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(guestbook_entries, file, ensure_ascii=False, indent=2)
    return jsonify(entry), 201

if __name__ == '__main__':
    app.run(debug=True)
