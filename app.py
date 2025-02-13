from flask import Flask, render_template, request, redirect, url_for
from generate_script import generate_voiceover_script
import database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        niche = request.form['niche']
        script = generate_voiceover_script(niche)
        return render_template('index.html', script=script)
    
    return render_template('index.html', script=None)

if __name__ == "__main__":
    database.init_db()  # Ensure the database is ready
    app.run(debug=True)

