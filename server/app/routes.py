from flask import Blueprint
from app.controllers.restaurant import get_restaurant,delete_restaurant

bp=Blueprint('bp', __name__)

@bp.route('/')
def home():
    return 'welcome home'
@bp.route('/restaurant', methods=['GET'])
def add_user():
    return get_restaurant()

@bp.route('/restaurant/<int:id>', methods=['GET'])
def list_users():
    return delete_restaurant(id)

