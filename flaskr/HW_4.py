from flask import Blueprint, render_template
from project.db import get_db

hw4 = Blueprint('hw4', __name__, url_prefix='/hw4')

@hw4.route('/names/')
def names():
    db = get_db()
    artists = db.execute(
        'SELECT DISTINCT artist FROM tracks'
    ).fetchall()
    artist_names = [row['artist'] for row in artists]
    return render_template('names.html', artists=artist_names)