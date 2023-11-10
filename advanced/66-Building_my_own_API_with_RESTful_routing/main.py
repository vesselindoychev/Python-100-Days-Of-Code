import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

API_KEY = 'TopSecretAPIKey'


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)
    return jsonify(cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    all_cafes = []
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    for c in cafes:
        all_cafes.append(c.to_dict())
    return jsonify(all_cafes)


@app.route('/search')
def search_for_a_particular_cafe():
    query_location = request.args.get('loc')
    current_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()

    if current_cafes:
        return jsonify([cafe.to_dict() for cafe in current_cafes])
    return jsonify({'Not Found': 'Sorry, we don\'t have a cafe at that location.'}), 404


@app.route('/add', methods=['POST'])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.args.get('name'),
        map_url=request.args.get('map_url'),
        img_url=request.args.get('img_url'),
        location=request.args.get('location'),
        seats=request.args.get('seats'),
        has_toilet=bool(request.args.get('has_toilet')),
        has_wifi=bool(request.args.get('has_wifi')),
        has_sockets=bool(request.args.get('has_sockets')),
        can_take_calls=bool(request.args.get('can_take_calls')),
        coffee_price=request.args.get('coffee_price'),
    )

    if request.method == 'POST':
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({'success': 'You have successfully added new cafe.'})


@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_cafe_price(id):
    query_new_price = request.args.get('new_price')

    current_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    # cafe = db.get_or_404(Cafe, id)
    if request.method == 'PATCH':
        if current_cafe:
            current_cafe.coffee_price = query_new_price
            db.session.commit()
            return jsonify({'Success': 'You have successfully updated the coffee price.'}), 200
        return jsonify(error={'Not Found': 'Sorry, a cafe with that id was not found in the database.'}), 404


@app.route('/report-closed/<int:id>', methods=['DELETE'])
def delete_cafe(id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
    api_key = request.args.get('api-key')
    if request.method == 'DELETE':
        if cafe:
            if api_key == API_KEY:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={'Success': 'You have successfully deleted this cafe.'}), 200
            return jsonify(error={'Forbidden': 'Sorry,that\' not allowed. Make sure you have the correct api-key.'}), 401
        return jsonify(error={'Not Found': 'Sorry, a cafe with that id was not found in the database.'}), 404


        ## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
