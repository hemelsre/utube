from flask import Blueprint, render_template, request
from generate_script import generate_voiceover_script
from scheduler import start_scheduler, stop_scheduler
from database import get_niches, get_script_count

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def dashboard():
    niches = get_niches()
    counts = get_script_count()
    return render_template('index.html', niches=niches, counts=counts)

@routes_bp.route('/generate', methods=['POST'])
def generate():
    niche = request.form['niche']
    script = generate_voiceover_script(niche)
    return render_template('index.html', script=script)
