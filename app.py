from flask import Flask, render_template, request, jsonify
import openai
from config import OPENAI_API_KEY, DB_CONFIG

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_script', methods=['POST'])
def generate_script():
    niche = request.form.get('niche')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Generate a voice-over script for YouTube videos."},
                      {"role": "user", "content": f"Generate a script about {niche}"}]
        )
        script = response.choices[0].message['content']
    except Exception as e:
        script = f"Error: {str(e)}"
    return jsonify({'script': script})

@app.route('/test_script', methods=['GET'])
def test_script():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Test ChatGPT script generation for a YouTube voice-over."}]
        )
        test_output = response.choices[0].message['content']
    except Exception as e:
        test_output = f"Error: {str(e)}"
    return jsonify({'output': test_output})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)