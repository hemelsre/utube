from flask import Flask, render_template, request, jsonify
from database import get_latest_script_from_db  # Import database function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_script', methods=['GET'])
def test_script():
    script = get_latest_script_from_db()  # Fetch from DB
    return jsonify({'script': script})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)