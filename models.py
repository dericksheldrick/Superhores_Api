from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata =metadata)

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers":[hp.to_dict() for hp in self.hero_powers]
        }

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    description= db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete-orphan")

    @validates('description')
    def validate_description(self, key, value):

        if not value or len(value) < 20:
            raise ValueError("Description should be atleast 20  caharcters")
        
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description":self.description
        }
    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strenths must be 'Strong', 'Weak', or 'Average'")
        return value
    
    def to_dict(self):
        return {
            "id":self.id,
            "strength":self.strength,
            "hero_id":self.hero_id,
            "power_id":self.power_id,
            "hero":{
                "id":self.hero.id,
                "name":self.hero.name,
                "super_name":self.hero.super_name
            },
            "power": self.power.to_dict()
        }