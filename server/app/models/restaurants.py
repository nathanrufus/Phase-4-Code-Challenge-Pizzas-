from app import db

class Restaurant(db.Model):
    __tablename__='restaurant'
    id=db.Column(db.Integer(),primary_key=True)
    name =db.Column(db.String(100))
    address =db.Column(db.String(100))


    def serialize(self):
        {
            'id':'self.id',
            'id':'self.name',
            'id':'self.address'
        }


