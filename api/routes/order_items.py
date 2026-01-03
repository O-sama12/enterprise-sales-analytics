from flask import Blueprint, request, jsonify
from api.services.order_item_service import OrderItemService
order_items_bp = Blueprint('order_items', __name__)
@order_items_bp.route('/order-items', methods=["POST"])
def create_order_item():
    data = request.get_json()
    order_item_id = OrderItemService.create_order_item(
        data['order_id'],
        data['product_id'],
        data['quantity'],
        data.get("discount", 0)
    )
    return jsonify({
        "order_item_id": order_item_id,
        "message": "Order item created"
    }), 201