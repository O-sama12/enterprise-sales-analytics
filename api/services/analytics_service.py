from db.connection import get_db_connection

class AnalyticsService:
    @staticmethod
    def get_total_revenue():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary = True)
        query = """
            SELECT 
            ROUND(SUM(oi.quantity * p.price * (1 - oi.discount)), 2) AS total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
"""
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result["total_revenue"] or 0
    @staticmethod
    def get_revenue_by_region():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT
            r.region_name,
            ROUND(SUM(oi.quantity * p.price * (1 - oi.discount)), 2) AS revenue
        FROM regions r
        JOIN customers c ON r.region_id = c.region_id
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY r.region_name
        ORDER BY revenue DESC
        """

        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results
