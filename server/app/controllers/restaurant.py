from flask import request, jsonify,make_response
from app import db
from app.models.restaurants import Restaurant


def get_restaurant(id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return {"error": "404 restaurant not found"}, 404

        response = make_response(jsonify(restaurant.to_dict()), 200)
        return response

def delete_restaurant(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return {"error": "404 restaurant not found"}, 404

        db.session.delete(restaurant)
        db.session.commit()

        return {}, 200
  
