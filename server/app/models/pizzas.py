from app import db
from sqlalchemy_serializer import SerializerMixin

class Pizzas(db.Model,SerializerMixin):
    __tablename__ = "pizzas"
    serialize_rules = ('-restaurants.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    ingredients = db.Column(db.String, nullable=False)

    restaurants = db.relationship(
        'RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f"<Pizza id:{self.id}, name:{self.name}>"
    
   