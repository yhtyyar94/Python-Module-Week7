from connect import connect


def create_database_if_not_exists(dbname):
    # Connect to the PostgreSQL server
    conn = connect("crm")
    conn.autocommit = True
    cur = conn.cursor()

    # Check if the database exists
    cur.execute(("SELECT 1 FROM pg_database WHERE datname = %s"), [dbname])
    exists = cur.fetchone()

    if not exists:
        # Create the database
        cur.execute("CREATE DATABASE {}".format(dbname))
        print(f"Database '{dbname}' created successfully.")
    else:
        print(f"Database '{dbname}' already exists.")

    # Close the connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Example usage
    create_database_if_not_exists("crm")
