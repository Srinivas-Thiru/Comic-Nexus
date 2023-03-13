import sqlite3

def main():
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM inventory WHERE user_id = 1")
        global items
        items = c.fetchall()
        conn.close()
        print(type(items[0]))
        l = []
        for i in items:
            l.append(i[0])
        print(l) 
                

main()