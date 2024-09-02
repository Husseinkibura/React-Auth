from flask import Blueprint, request, jsonify
from extensions import db
from models import Item

bp = Blueprint('item', __name__)

@bp.route('/create-item', methods=['POST'])
def create_item():
    # (your existing create-item code)
    pass

@bp.route('/items', methods=['GET'])
def get_items():
    # (your existing get-items code)
    pass

@bp.route('/update-item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # (your existing update-item code)
    pass

@bp.route('/delete-item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # (your existing delete-item code)
    pass
