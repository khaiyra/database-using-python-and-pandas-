# import library

import psycopg2
from psycopg2 import Error

# function to create connection

def getConnection():
    # create connection
    connection = psycopg2.connect(
        host = 'localhost', user = 'postgres', password = '1234', database = 'postgres'
    )
    return connection

def closeConnection(connection):
    connection.close()
    print('Connection is Closed')

def getCustomer(customer_id):
    try:
        connection = getConnection() # create connection
        cursor = connection.cursor() # create cursor


        query = 'SELECT * FROM CUSTOMER WHERE customer_id = %s' # query to fetch customer

        cursor.execute(query, (customer_id,))
        records = cursor.fetchall() # object that will hold the records

        print('Printing Records')

        for row in records:
            print("Customer ID", row[0])
            print("Store ID", row[1])
            print("First Name", row[2])
            print("Last Name", row[3])
            print("Email", row[4])
            print("Address ID", row[5])
            print("Active Status", row[6])
            print("Create Date", row[7])
            print("Last Update", row[8])
            print("Active", row[9], '\n')

        closeConnection(connection) # close connection
    except Error as e:
        print("Error: Reading Record")

# print out customer information
getCustomer(34)