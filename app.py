from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Hero, Power, HeroPower


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return{'message': 'Superheroes API'}

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    return jsonify(hero.to_dict()), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error":"Power not found"}), 404
    
    data = request.get_json()
    try:
        if "description" in data:
            power.description = data["description"]

        db.session.commit()
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    
    return jsonify(power.to_dict()), 200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hp = HeroPower(
            strength = data['strength'],
            hero_id = data["hero_id"],
            power_id = data["power_id"]
        )
        db.session.add(new_hp)
        db.session.commit()

        hero = Hero.query.get(data["hero_id"])
        return jsonify(hero.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": [str(e)]}), 400
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)