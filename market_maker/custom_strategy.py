import sys

from market_maker.market_maker import OrderManager


class CustomOrderManager(OrderManager):
    """A sample order manager for implementing your own custom strategy"""

    def place_orders(self) -> None:
        # implement your custom strategy here

        buy_orders = []
        sell_orders = []

        # populate buy and sell orders, e.g.
        buy_orders.append({'price': 999.0, 'orderQty': 100, 'side': "Buy"})
        sell_orders.append({'price': 1001.0, 'orderQty': 100, 'side': "Sell"})

        self.converge_orders(buy_orders, sell_orders)

    def createOrder(self, price, side, orderQty) -> None:
        orderMap = {}
        orderMap['price'] = price
        orderMap['orderQty'] = orderQty
        orderMap['side'] = side
        #We create a "LONG" or "SHORT" orders and append them into the order placer
        return orderMap

    def adjustStop(self, price, side) -> None:
        ##Adjusts the current orders in the book to match the new trend lines
        return -1
    
    

def run() -> None:
    order_manager = CustomOrderManager()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        order_manager.run_loop()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
