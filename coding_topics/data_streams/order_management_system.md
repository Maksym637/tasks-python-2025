```python

class OrderManagementSystem:
    def __init__(self):
        self.orders = {}

    def add_item(self, order_id: str, item_id: str, quantity: int, price: float) -> bool:
        if price < 0 or quantity < 0:
            return False

        if order_id not in self.orders:
            self.orders[order_id] = {}

        self.orders[order_id][item_id] = {"quantity": quantity, "price": price}

        return True

    def get_item(self, order_id: str, item_id: str) -> dict | None:
        if order_id in self.orders and item_id in self.orders[order_id]:
            item = self.orders[order_id][item_id]
            return {"quantity": item["quantity"], "price": item["price"]}

        return None

    def delete_item(self, order_id: str, item_id: str) -> bool:
        if order_id in self.orders and item_id in self.orders[order_id]:
            del self.orders[order_id][item_id]

            if not self.orders[order_id]:
                del self.orders[order_id]
            return True

        return False

    def aggregate_order(self, order_id: str) -> dict | None:
        initialized_stats = {
            "total_quantity": 0,
            "total_price": 0.0,
            "items": []
        }

        if order_id not in self.orders:
            return None

        items = self.orders[order_id]

        if not items:
            return initialized_stats

        for item_id, item_info in items.items():
            quantity, price = item_info["quantity"], item_info["price"]

            if price > 0:
                initialized_stats["total_quantity"] += quantity
                initialized_stats["total_price"] += price * quantity
                initialized_stats["items"].append({
                    "item_id": item_id,
                    "quantity": quantity,
                    "price": price
                })

        return initialized_stats

```
