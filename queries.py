def execute_query(cursor, filename):
    with open(filename, "r") as file:
        query = file.read()
        cursor.execute(query)
        return cursor.fetchall()
