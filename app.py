from flask import Flask, render_template, request, jsonify
from config import OPENAI_API_KEY, DB_CONFIG  # Import API key and DB config
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_script', methods=['POST'])
def generate_script():
    niche = request.form.get('niche')
    script = f"Generated script for niche: {niche} using API key: {OPENAI_API_KEY[:5]}..."  # Placeholder
    return jsonify({'script': script})

@app.route('/test_script', methods=['GET'])
def test_script():
    test_output = "Test output from ChatGPT script generation using API key."  # Placeholder
    return jsonify({'output': test_output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)