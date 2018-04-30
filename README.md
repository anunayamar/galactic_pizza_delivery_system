# galactic_pizza_delivery_system

It is a galactic pizza delivery system.

Takes input in json format:

```
{"orderId": 100, "status": "NEW", "updateId": 287,
"amount": 20}
{"orderId": 100, "status": "COOKING", "updateId": 289,
"cookTime": 7}
{"orderId": 100, "status": "COOKING", "updateId": 289,
"cookTime": 7}
{"orderId": 101, "status": "NEW", "updateId": 289,
"amount": 13}
{"orderId": 100, "status": "DELIVERING", "updateId": 294}
{"orderId": 102, "status": "NEW", "updateId": 291,
"amount": 17}
{"orderId": 101, "status": "CANCELED", "updateId": 290}
```

It generates order summary in the following format:
```
New: 0
Cooking: 1
Delivering: 1
Delivered: 0
Canceled: 1
Refunded: 0
Total amount charged: $37

```

The code has been written using Python 3.6
