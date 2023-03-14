#SRINIVAS_THIRUGNANASELVAM
#WEB BOOK APPLICATION USING FLASK


from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3


app = Flask(__name__, static_url_path = "/static")
app.secret_key = "mysecretkey"

class Db:

    def __init__(self):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM comics")
        lis = c.fetchall()
        conn.close()
        self.List = sorted(lis)

db = Db()

class LoginRegister:
        
    @app.route("/")
    def index():
        return redirect(url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = c.fetchone()
            conn.close()
            if user is None:
                return render_template("login.html", error="Invalid username or password")
            else:
                session["user_id"] = user[0]
                return redirect(url_for("inventory"))
        else:
            return render_template("login.html")
        
            
    @app.route("/admin", methods=["GET","POST"])
    def admin_login():    
        if request.method == "POST":    
            username = request.form["username"]
            password = request.form["password"]
            if not username or username != "admin" :
                return render_template("admin.html", error = "Admin not found")
            else :
                if not password or password != "password":
                    return render_template("admin.html", error = "Admin not found")
                else:
                    conn = sqlite3.connect("database.db")
                    c = conn.cursor()
                    c.execute("SELECT username FROM users;")
                    usernames = c.fetchall()
                    c.execute("SELECT name FROM inventory;")
                    inventories = c.fetchall()
                    conn.close()
                    return render_template("database.html", names = usernames , inventories = inventories)
        else :
            return render_template("admin.html")
        

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            confirm_password = request.form["confirm_password"]
            if password != confirm_password:
                return render_template("register.html", error="Passwords do not match.")
            else:
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                try:
                    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                    conn.close()
                    return redirect(url_for("login"))
                except sqlite3.IntegrityError:
                    conn.close()
                    return render_template("register.html", error="Username already exists")
        else:
            return render_template("register.html")


class Inventory:

    @app.route("/inventory")
    def inventory():
        if "user_id" in session:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM inventory WHERE user_id = ?", (session["user_id"],))
            items = c.fetchall()
            conn.close()
            
            
            return render_template("inventory.html", items=sorted(items))
        else:
            return redirect(url_for("login"))

    @app.route("/add", methods=["GET", "POST"])
    def add():
        global lis
        if request.method == "POST":
            name = request.form["name"]
            quantity = request.form["quantity"]
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM inventory WHERE user_id = ?", (session["user_id"],))
            items = c.fetchall()
            conn.close()
                    
            namelist = []
            for i in items:
                namelist.append(i[0])        

            if name in namelist:
                return render_template("add.html", error = "Item already in your inventory", lis = db.List)
            else :
                conn = sqlite3.connect("database.db")
                c = conn.cursor()
                c.execute("INSERT OR IGNORE INTO inventory (name, quantity, user_id) VALUES (?, ?, ?)", (name, quantity, session["user_id"]))
                conn.commit()
                conn.close()
                
                return redirect("/inventory")
        else:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM comics")
            
            lis = c.fetchall()
            conn.close()
            return render_template("add.html", lis =db.List)

    @app.route("/remove/<int:item_id>", methods=['GET'])
    def remove(item_id):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("DELETE FROM inventory WHERE id = ? AND user_id = ?", (item_id, session["user_id"]))
        conn.commit()
        conn.close()
        return redirect("/inventory")

    @app.route("/logout")
    def logout():
        session.pop("user_id", None)
        return redirect("/login")


if __name__ == "__main__":
    app.run()
