from flask import Flask
from api.routes.customers import customers_bp
from api.routes.orders import orders_bp
from api.routes.order_items import order_items_bp
app = Flask(__name__)
app.register_blueprint(customers_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(order_items_bp, url_prefix="/api")
if __name__ == "__main__":
    app.run(debug=True)