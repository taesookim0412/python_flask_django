import flask from flask
app = flask(__name__)
@app.route('/dojo')

def dojo():
    return "Dojo!"

if __name__=="__main__":
    app.run(debug=True)