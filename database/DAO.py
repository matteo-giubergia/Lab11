from database.DB_connect import DBConnect
from model.product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary= True)
        res = []

        query = """select distinct year(`Date`) as anno
                    from go_daily_sales g"""

        cursor.execute(query)

        for row in cursor:
            res.append(row['anno'])

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select distinct gp.Product_color as color
                    from go_products gp """

        cursor.execute(query)

        for row in cursor:
            res.append(row['color'])

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getNodes(color):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select *
                    from go_products gp 
                    where gp.Product_color =%s  
                     """

        cursor.execute(query, (color, ))

        for row in cursor:
            res.append(Product(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getArchi(color, color2, anno, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select g1.Product_number as p1, g2.Product_number as p2, count(distinct g1.`Date`) as peso
                    from (select Product_number  
                            from go_products gp 	
                            where gp.Product_color =%s) as prod1,
                            (select Product_number  
                            from go_products gp 	
                            where gp.Product_color =%s) as prod2, go_daily_sales g1, go_daily_sales g2
                    where g1.Product_number < g2.Product_number 
                    and g1.Product_number=prod1.Product_number 
                    and g2.Product_number=prod2.Product_number 
                    and g1.Retailer_code = g2.Retailer_code 
                    and year(g1.`Date`) = %s 
                    and g1.`Date`=g2.`Date` 
                    group by p1, p2  
                         """

        cursor.execute(query, (color, color2, anno))

        for row in cursor:
            res.append((idMap[row['p1']], idMap[row['p2']], row['peso']))

        cursor.close()
        conn.close()
        return res



