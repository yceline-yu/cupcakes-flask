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

    return (jsonify(cupcakes=serialized), 200)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake_data(cupcake_id):
    """get data on a single cupcake, return JSON"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)


@app.route('/api/cupcakes', methods=["POST"])
def add_new_cupcake():
    """add new cupcake to DB, return JSON"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] if request.json["image"] else None

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def edit_cupcake_data(cupcake_id):
    """edit cupcake and send to DB, return JSON
    ==> {cupcake: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] if request.json["image"] else None

    cupcake.flavor = flavor if flavor else cupcake.flavor
    cupcake.size = size if size else cupcake.size
    cupcake.rating = rating if rating else cupcake.rating
    cupcake.image = image if image else cupcake.image

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake_data(cupcake_id):
    """remove cupcake from DB, return JSON confirming 
    ==> {message: "Deleted"}.
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="Deleted")
