import upstox_client


class UpstoxAPI:
    def __init__(self, access_token):
        self.configuration = upstox_client.Configuration()
        self.configuration.access_token = access_token
        self.api_client = upstox_client.ApiClient(self.configuration)

    def place_order(self, stock_name, ltp, quantity, stoploss):
        order = upstox_client.Order(
            symbol=stock_name,
            exchange="NSE",
            instrument_type="EQ",
            quantity=quantity,
            price=ltp,
            stop_loss=stoploss,
            transaction_type="BUY"
        )
        api_response = self.api_client.place_order(order)
        return api_response