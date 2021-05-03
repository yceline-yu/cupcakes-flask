"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

# from flask_debugtoolbar import DebugToolbarExtension
# toolbar = DebugToolbarExtension(app)

# comment out if you want to see/pause redirects 
# app.config[‘DEBUG_TB_INTERCEPT_REDIRECTS’] = False

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/api/cupcakes')
def get_cupcake_list():
    """get data of all cupcakes, return JSON"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_data(cupcake_id):
    """get data on a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()
    
    return jsonify(cupcake=serialized)
