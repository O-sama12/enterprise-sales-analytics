from flask import Blueprint, jsonify
from api.services.analytics_service import AnalyticsService

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/total-revenue", methods=["GET"])
def total_revenue():
    revenue = AnalyticsService.get_total_revenue()
    return jsonify({
        "total_revenue": revenue
    }), 200
@analytics_bp.route("/revenue-by-region", methods=["GET"])
def revenue_by_region():
    data = AnalyticsService.get_revenue_by_region()
    return jsonify(data), 200
