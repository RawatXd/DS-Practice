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

    cursor = connection.cursor(dictionary=True)
    return connection,cursor

def fetch_all_records():
    connection,cursor = get_db_cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()


def fetch_expense_for_date(expense_date):
    connection, cursor = get_db_cursor()
    cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()



if __name__ == "__main__":
    fetch_all_records()
    fetch_expense_for_date("2024-08-01")