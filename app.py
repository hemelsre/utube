from flask import Flask, render_template, request, jsonify
import openai
from config import OPENAI_API_KEY, DB_CONFIG  # Import API key and database config

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Route for homepage that serves the web UI
@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML UI

# Route for generating voice-over scripts based on user-provided niche
@app.route('/generate_script', methods=['POST'])
def generate_script():
    niche = request.form.get('niche')  # Get niche from form data
    try:
        # Call OpenAI API to generate script using the latest API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Generate a voice-over script for YouTube videos."},
                {"role": "user", "content": f"Generate a script about {niche}"}
            ]
        )
        script = response.choices[0].message.content  # Extract script content
    except Exception as e:
        script = f"Error: {str(e)}"  # Handle and display errors
    return jsonify({'script': script})  # Return script as JSON response

# Route for testing API integration with a sample script generation
@app.route('/test_script', methods=['GET'])
def test_script():
    try:
        # Call OpenAI API for a test output
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Test ChatGPT script generation for a YouTube voice-over."}]
        )
        test_output = response.choices[0].message.content  # Extract test output
    except Exception as e:
        test_output = f"Error: {str(e)}"  # Handle errors
    return jsonify({'output': test_output})  # Return test output as JSON response

# Main entry point to run the app on specified host and port
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)