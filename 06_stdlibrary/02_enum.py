from enum import Enum


class OrderStatus(Enum):
    PENDING = 'pending'
    SHIPPING = 'shipping'
    DELIVERED = 'delivered'

def process_order(status):
    if status == OrderStatus.PENDING:
        return '注文処理中...'
    elif status == OrderStatus.SHIPPING:
        return '配送中...'
    elif status == OrderStatus.DELIVERED:
        return '配送完了'
    
order_status = OrderStatus.SHIPPING
result = process_order(order_status)
print(result)
order_status = OrderStatus('pending')
print(order_status, order_status.name, order_status.value)

class Difficulty(Enum):
    EASY=1
    HARD=2

def difficulty_level(level):
    if level == Difficulty.EASY:
        # 簡単な場合の処理
        pass
    