from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")

def index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db('SELECT * FROM friends;')
    print(friends)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)