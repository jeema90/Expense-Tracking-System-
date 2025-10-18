import mysql.connector
from contextlib import contextmanager
import logging
import sys
from pathlib import Path
from datetime import datetime

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.resolve()))
from backend.paths import DB_FILE
import logging_setup

from logging_setup import logging_setup
from paths import DB_FILE

logger = logging_setup("db_helper")


# Generator / context manager to handle DB connection and cursor
@contextmanager
def get_db_cursor():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="star&daisy1",
        database="expense_manager",
        autocommit = True
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor  # give cursor to the caller
    finally:
        cursor.close()
        connection.close()

# Fetch all records
def get_all_records():

    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        logger.info(f"data fetched for all the expense dates:{expenses}")
        return expenses

# Fetch records for a specific date
def get_expenses_for_date(expense_date):

    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        logger.info(f"data fetched for the expense date:{expense_date},{expenses}")
        return expenses
def insert_expense(expense_date,amount,category,notes):

    with get_db_cursor() as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))
    logger.info(f"data inserted for the expense date:{expense_date, amount, category, notes}")

def delete_expense_for_a_date(expense_date):

    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s",(expense_date,))
    logger.info(f"data deleted for the expense date:{expense_date}")

def fetch_expense_summary(start_date, end_date):
        # Convert strings to datetime.date if needed
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date).date()
        if isinstance(end_date, str):
            end_date = datetime.fromisoformat(end_date).date()

        start_str = start_date.isoformat()
        end_str = end_date.isoformat()

        logger.info(f"data summary fetched for the expense dates:{start_date},{end_date}")
        with get_db_cursor() as cursor:
            cursor.execute('''SELECT category,sum(amount) as total 
            FROM expenses
            where expense_date between %s and %s
            group by category''',(start_str,end_str))
            expenses = cursor.fetchall()
            print(f"Fetching data from {start_str} to {end_str}")
            return expenses


def fetch_expense_summary_by_month():
    logger.info(f"data summary fetched for the all expenses by month")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT 
            DATE_FORMAT(expense_date, '%m') AS month,
            SUM(amount) AS total
            FROM expenses
            GROUP BY month
            ORDER BY month;''')
        expenses = cursor.fetchall()
        print(f"Fetching data of all months")
        return expenses


# Main block
if __name__ == "__main__":
    print("script started")
    get_all_records()
    get_expenses_for_date("2024-08-01")
    insert_expense("2024-08-25","40","food","butter")
    get_expenses_for_date("2024-08-25")
    #delete_expense_for_a_date("2024-08-25")
    summary=fetch_expense_summary("2024-08-02","2024-08-06")
    print(summary)
    logger.info(f"Expense summary: {summary}")
    overall=fetch_expense_summary_by_month()
    print(overall)
