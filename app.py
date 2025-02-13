from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/test_script')
def test_script():
    script = get_latest_script_from_db()  # Fetch from DB
    return jsonify({'script': script})

if __name__ == "__main__":
    app.run()