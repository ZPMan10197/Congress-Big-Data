import mysql.connector

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="politics"
    )

def create_record(conn, name, political_party, state, office_held):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO politicians (name, political_party, state, office_held) "
        "VALUES (%s, %s, %s, %s)",
        (name, political_party, state, office_held)
    )
    conn.commit()

def read_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM politicians")
    return cursor.fetchall()

def update_record(conn, id, name, political_party, state, office_held):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE politicians "
        "SET name = %s, political_party = %s, state = %s, office_held = %s "
        "WHERE id = %s",
        (name, political_party, state, office_held, id)
    )
    conn.commit()

def delete_record(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM politicians WHERE id = %s", (id,))
    conn.commit()
