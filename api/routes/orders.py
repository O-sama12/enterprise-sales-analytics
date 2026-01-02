from flask import Blueprint, request, jsonify
from api.services.order_service import OrderService
orders_bp = Blueprint('orders', __name__)
@orders_bp.route('/orders', methods=["POST"])
def create_order():
    data = request.json
    order_id = OrderService.create_order(
        data["customer_id"],
        data["order_date"],
        data["status"],
    )
    return jsonify({
        "message": "Order created",
        "order_id": order_id
    }), 201