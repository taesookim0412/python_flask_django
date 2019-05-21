from flask import Flask
app = Flask(__name__)
@app.route('/repeat/<num>/<phrase>')
def repeat_phrase(num, phrase):
    newphrase = ""
    for i in range(0, int(num)):
        newphrase += phrase
    return newphrase
if __name__=="__main__":
    app.run(debug=True)