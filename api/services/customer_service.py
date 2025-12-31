from db.connection import get_db_connection
class CustomerService:
    @staticmethod
    def create_customer(name, region_id, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO customers (customer_name, email, region_id) VALUES (%s, %s, %s)"""
        cursor.execute(query, (name, email, region_id))
        conn.commit()
        customer_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return customer_id
   
    @staticmethod
    def get_all_customers():
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """SELECT * FROM customers"""
        cursor.execute(query)
        customers = cursor.fetchall()
        cursor.close()
        conn.close()
        return customers