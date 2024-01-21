from flask import request, jsonify,make_response
from app.models.pizzas import Pizzas

def get_pizzas():
        pizzas = [pizza.to_dict()
                  for pizza in Pizzas.query.all()]
        response = make_response(jsonify(pizzas), 200)
        return response

