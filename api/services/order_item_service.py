from db.connection import get_db_connection
class OrderItemService:
    @staticmethod
    def create_order_item(order_id, product_id, quantity, discount):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO order_items (order_id, product_id, quantity, discount) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (order_id, product_id, quantity, discount))
        conn.commit()
        order_item_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return order_item_id