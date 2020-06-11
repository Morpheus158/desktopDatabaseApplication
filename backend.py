import psycopg2

def table_create():
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id SERIAL, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def view_all():
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def search_entry(title="", author="", year="", isbn=""):
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def add_entry(title, author, year, isbn):
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (DEFAULT,%s,%s,%s,%s)", (title, author, year, isbn))
    con.commit()
    con.close()

def update_selected(id, title, author, year, isbn):
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, id))
    con.commit()
    con.close()

def delete_selected(id):
    con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=%s", (id, ))
    con.commit()
    con.close()

table_create()