from flask import Flask, request, jsonify

class TradingApp:
    def __init__(self, upstox_api):
        self.upstox_api = upstox_api
        self.app = Flask(__name__)

    def create_routes(self):
        @self.app.route('/place_order', methods=['POST'])
        def place_order():
            data = request.get_json()
            stock_name = data['stock_name']
            ltp = data['ltp']
            quantity = data['quantity']
            stoploss = data['stoploss']
            api_response = self.upstox_api.place_order(stock_name, ltp, quantity, stoploss)
            return jsonify(api_response)

    def run(self):
        self.create_routes()
        self.app.run(debug=True)