from flask import render_template
from ..app import app
from flask_example.data_utils.data_utils import DataUtils
from flask_example.photos import get_photos
from flask import request, redirect

du = DataUtils()


@app.route('/')
def index():
    girl_first, girl_second = get_photos()

    try:
        girl_winner = request.args.get('girl_first')
        girl_looser = request.args.get('girl_second')
        du.update_rating({girl_winner: 1, girl_looser: 0})
        redirect('/')
    except:
        pass

    return render_template('index.html', girl_first=girl_first, girl_second=girl_second)


@app.route('/top_100')
def top_hindret():
    return render_template('top_100.html', girls=du.get_top())

