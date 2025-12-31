from flask import Blueprint, request, jsonify
from api.services.customer_service import CustomerService
customers_bp = Blueprint('customers', __name__)
@customers_bp.route('/customers', methods=["POST"])
def create_customer():
    data = request.json
    customer_id = CustomerService.create_customer(
        data["name"],
        data["region_id"],
        data.get("email"),
    )
    return jsonify({
        "message": "Customer created",
        "customer_id": customer_id
    }), 201
@customers_bp.route("/customers", methods=["GET"])
def get_customers():
    customers = CustomerService.get_all_customers()
    return jsonify(customers), 200