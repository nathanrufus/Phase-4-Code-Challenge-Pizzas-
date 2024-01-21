from app import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = "restaurant_pizza"
    serialize_rules = ('-pizza.restaurants',
                       '-restaurant.pizzas')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    pizza = db.relationship('Pizza', back_populates='restaurants')
    restaurant = db.relationship(
        'Restaurant', back_populates='pizzas')

    @validates('price')
    def validate_price(self, key, price):
        if 1 <= price <= 30:
            return price
        raise ValueError('price should range between 1 and 30')

    def __repr__(self):
        return f"<RestaurantPizza id:{self.id}, res:{self.restaurant_id}, pizza:{self.pizza_id}>"