from flask import Blueprint, render_template
from database import get_niches_with_counts

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def dashboard():
    niches = []
    counts = {}

    try:
        niches, counts = get_niches_with_counts()
    except Exception as e:
        print(f"Error fetching niches: {e}")

    if niches is None:
        niches = []
    if counts is None:
        counts = {}

    return render_template('index.html', niches=niches, counts=counts)
