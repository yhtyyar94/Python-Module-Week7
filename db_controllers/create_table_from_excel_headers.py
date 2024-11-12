from connect import connect
from backend.read_xlsx import read_xlsx


def create_table_from_excel_headers(file_name, table_name):
    # Read the Excel file
    rows = read_xlsx(file_name)

    # Extract headers
    headers = rows[0]

    # Generate SQL statement
    columns = ", ".join([f'"{header}" TEXT' for header in headers])
    create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns});'

    # Connect to PostgreSQL and execute the query
    conn = connect()
    cur = conn.cursor()
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

    print(f'Table "{table_name}" created successfully.')
