from backend.read_xlsx import read_xlsx
from connect import connect


def insert_records_from_excel(file_name, table_name):
    # Read the Excel file
    rows = read_xlsx(file_name)

    # Extract headers and records
    headers = rows[0]
    records = rows[1:]

    # Generate SQL INSERT statement
    columns = ", ".join([f'"{header}"' for header in headers])
    placeholders = ", ".join(["%s"] * len(headers))
    insert_query = f'INSERT INTO "{table_name}" ({columns}) VALUES ({placeholders})'

    # Connect to PostgreSQL and execute the query
    conn = connect()
    cur = conn.cursor()
    try:
        for record in records:
            cur.execute(insert_query, record)
        conn.commit()
        print(f"Records inserted successfully into '{table_name}' table.")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
