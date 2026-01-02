from db.connection import get_db_connection
class OrderService:
    @staticmethod
    def create_order(customer_id, order_date, status):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ORDERS (customer_id, order_date, status) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (customer_id, order_date, status))
        conn.commit()
        order_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return order_id