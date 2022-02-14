from flask import Flask, redirect, render_template, session, request 
import random
app = Flask(__name__)
app.secret_key = "bippityboppitybleepbloopblopbip"



@app.route('/')
def index():
    if 'gold' not in session:
        session ['gold'] = 0
        session ['message'] = []
    return render_template('index.html')



@app.route('/process_money', methods=["POST"])
def process_money():
    building = request.form['building']
    value = 0

    if building == "farm":
        value = random.randint(10,20)
    elif building == "cave":
        value = random.randint(5,10)
    elif building == "house":
        value = random.randint(2,5)
    elif building == "casino":
        value == random.randint(-50,50)

    session['gold'] += value 
    return redirect('/')

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)