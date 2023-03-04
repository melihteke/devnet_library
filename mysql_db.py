import mysql.connector
import environment



class MySQLDatabase:
    def __init__(self, host=environment.HOME_MYSQL_HOST, user=environment.HOME_MYSQL_USERNAME, password=environment.HOME_MYSQL_PASSWORD, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
    
    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
    
    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            results = cursor.fetchall()
            self.connection.commit()
            return results
        except mysql.connector.Error as error:
            print(f"Error executing query: {error}")
        finally:
            cursor.close()
        
    def insert_data(self, table, data):
        columns = ", ".join(data.keys())
        values = tuple(data.values())
        placeholders = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        return self.execute_query(query, values)
    
    def select_data(self, table, columns="*", where=None, values=None):
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += f" WHERE {where}"
        return self.execute_query(query, values)
    
    def update_data(self, table, data, where=None, values=None):
        set_values = ", ".join([f"{column}=%s" for column in data.keys()])
        query = f"UPDATE {table} SET {set_values}"
        if where:
            query += f" WHERE {where}"
        values = tuple(data.values()) + values if values else tuple(data.values())
        return self.execute_query(query, values)
    
    def delete_data(self, table, where=None, values=None):
        query = f"DELETE FROM {table}"
        if where:
            query += f" WHERE {where}"
        return self.execute_query(query, values)

'''
Delete: 
>>> a.connect()
>>> a.delete_data("site_table", "site_id=%s", (2310,))
[]

Update:
>>> data = {
...     "site_contact": "Jane Smith",
...     "site_city": "San Francisco"
... }
>>> a.update_data("site_table", data, "site_id=%s", (2498,))

Insert:
>>> data = {
...     "site_id": 1234,
...     "site_contact": "John Doe",
...     "site_continent": "NA",
...     "site_city": "New York",
...     "site_datacenter": "Equinix",
...     "site_status": 1
... }
>>> a.insert_data("site_table", data)


Select
>>> a.select_data('site_table', columns='*', where='site_id=%s', values=(2232,))
[(3, 2232, 'Joe Teke', 'US', 'Newyork', 'Equinix', 1)]
>>> 
>>> 
>>> a.select_data('site_table', columns='site_id, site_contact', where='site_id=%s', values=(2232,))
[(2232, 'John Teke')]



'''