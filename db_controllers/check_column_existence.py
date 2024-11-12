from connect import connect


def check_column_existence(table_name, column_name):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM information_schema.columns WHERE table_name = %s AND column_name = %s",
            (table_name, column_name),
        )
        return bool(cur.fetchone())


if __name__ == "__main__":
    table_name = "actor"
    column_name = "first_name"
    print(check_column_existence(table_name, column_name))
