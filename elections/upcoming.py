from elections.us_states import postal_abbreviations
import mvp
import flask

from flask import (
    Flask,Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)

bp = Blueprint('address_form', __name__, url_prefix='/')

@bp.route('/search', methods=('GET', 'POST'))
@bp.route('/')
def search():
    """Take in an address."""
    if request.method == 'POST':
        city = request.form['city'].replace(" ", "_").lower()
        state = request.form['state'].lower()
        api_response = mvp.return_api_results(city,state)
        print(api_response)
        print(type(api_response))

        return render_template('election_results.html', election_results= api_response) #may not work, test first

    return render_template('address_form.html', states=postal_abbreviations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
