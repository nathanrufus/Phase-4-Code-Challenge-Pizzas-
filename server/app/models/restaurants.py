from app import db
from sqlalchemy_serializer import SerializerMixin


class Restaurant(db.Model,SerializerMixin):
    __tablename__ = "restaurants"
    serialize_rules = ('-pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)

    pizzas = db.relationship(
        'RestaurantPizza', back_populates='restaurant')

    def __repr__(self):
        return f"<Restaurant id:{self.id}, name:{self.name}>"

