from connect import connect


def check_table_existence(table_name):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT 1 FROM information_schema.tables WHERE table_name = %s",
            (table_name,),
        )
        return bool(cur.fetchone())


if __name__ == "__main__":
    table_name = "actor"
    print(check_table_existence(table_name))
