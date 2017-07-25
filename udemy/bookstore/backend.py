import sqlite3

def connect():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS BOOK (ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT,YEAR INTEGER,ISBN INTEGER)')
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO BOOK VALUES (NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM BOOK')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="", year="",isbn=""):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM BOOK WHERE TITLE=? OR AUTHOR=? OR YEAR = ? OR ISBN=?',(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM BOOK WHERE ID = ?',(id,))
    conn.commit()
    conn.close()

def update(id,title,author, year,isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('UPDATE BOOK SET AUTHOR=?,TITLE=?,YEAR=?,ISBN=? WHERE ID = ?',(author,title,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert('The Ground','John',1919,91651651)
#print(view())
#print(search(author='John'))
#delete(2)
#update(4,'Not Ground','Bibs',1996,25546)
#print(view())
