import mysql.connector

def get_db_cursor():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="killua@555",
        database='expense_manager',
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Failed in Connection to a database")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)




connection.close()