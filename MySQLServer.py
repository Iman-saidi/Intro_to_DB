import mysql.connector

# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def main():
    conn = None
    cursor = None
    try:
        # 1. Connect to MySQL server (adjust host/user/password as needed)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234'
        )
        # 2. Create a cursor to execute statements
        cursor = conn.cursor()
        
        # 3. Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # 4. Success message
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:
        # Handle any errors (including connection failures)
        print(f"Error: {e}")
        
    finally:
        # 5. Clean up: close cursor and connection
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
