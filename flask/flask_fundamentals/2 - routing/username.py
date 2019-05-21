from flask import Flask
app = Flask(__name__)
@app.route("/say/<user>")
def say_user(user):
    print(user)
    user = user.capitalize()
    return "Hi " + user + "!"
if __name__=="__main__":
    app.run(debug=True)