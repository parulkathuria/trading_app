from flask import Flask, request, jsonify
import upstox_client
from trading import TradingApp
from api import UpstoxAPI




if __name__ == '__main__':
    access_token = "YOUR_ACCESS_TOKEN"
    upstox_api = UpstoxAPI(access_token)
    trading_app = TradingApp(upstox_api)
    trading_app.run()