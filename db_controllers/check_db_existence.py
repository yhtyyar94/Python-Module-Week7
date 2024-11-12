from connect import connect


def check_db_existence(db_name):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        return bool(cur.fetchone())


if __name__ == "__main__":
    db_name = "dvdrental"
    print(check_db_existence(db_name))
