from flask import Flask
from api.routes.customers import customers_bp
app = Flask(__name__)
app.register_blueprint(customers_bp, url_prefix='/api')
print(app.url_map)
if __name__ == "__main__":
    app.run(debug=True)