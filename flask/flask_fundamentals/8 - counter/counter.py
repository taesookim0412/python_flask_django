from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'counterkey_'

@app.route('/')
def increment_counter():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] = session['counter'] + 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.pop('counter')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)