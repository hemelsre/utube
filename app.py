from flask import jsonify
@app.route('/test_script')
def test_script():
    script = get_latest_script_from_db()  # Fetch from DB
    return jsonify({'script': script})