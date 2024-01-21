from flask import request, jsonify,make_response
from app import db
from app.models.restaurantpizza import RestaurantPizza


def post_restaurantpizza():
        try:
            data = request.get_json()
            respiz = RestaurantPizza(**data)
            db.session.add(respiz)
            db.session.commit()
            return data.to_dict(), 204
        except ValueError as err:
            return {"errors": str(err)}, 401