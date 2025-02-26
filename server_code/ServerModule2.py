import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import pymysql



def connect_to_mysql():

    connection = pymysql.connect(host="your_mysql_host", 

                                user="your_username", 

                                password="your_password", 

                                database="your_database_name")

    return connection



@anvil.server.callable

def get_data_from_mysql():

    conn = connect_to_mysql()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM your_table")

    data = cursor.fetchall()

    conn.close()

    return data