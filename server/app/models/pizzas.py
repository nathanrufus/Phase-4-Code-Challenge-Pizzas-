from app import db

class Pizzas(db.Model):
    __tablename__='pizzas'
    id=db.Column(db.Integer(),primary_key=True)
    name =db.Column(db.String(100))
    ingredients =db.Column(db.String(100))


    def serialize(self):
        {
            'id':'self.id',
            'id':'self.name',
            'id':'self.ingredients'
        }