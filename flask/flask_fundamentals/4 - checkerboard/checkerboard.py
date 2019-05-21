from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<rows>')
def index(rows):
    colors = [ "red", "black"  ]
    lastcolor = "red"
    return render_template("index.html", rows=int(rows), colors=colors)
if __name__=="__main__":
    app.run(debug=True)