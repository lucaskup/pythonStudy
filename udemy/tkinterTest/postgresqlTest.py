import psycopg2

def getConnection():
    return psycopg2.connect("dbname='testepg' user='testepg' password='testepg123' host='localhost' port='5432'")
def create_table():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    cur.execute("INSERT INTO store VALUES('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()

def insert(item, quantity,price):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity, price,item):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()


insert('Xana', 1,130)
