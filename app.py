from flask import Flask, render_template
import data
from manage import Manage

manage = Manage()

app = Flask(__name__)

@app.context_processor
def inject_stage_and_region():
    return dict(departures = data.departures)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', tours = data.tours)

@app.route('/from/<direction>')
def direction(direction):
    return  render_template('direction.html', departure = manage.depart_city(direction), direction = direction)

@app.route('/tour/<id>')
def tour(id):
    return  render_template('tour.html', tour = data.tours.get(int(id)))






if __name__=="__main__":
    app.run()
