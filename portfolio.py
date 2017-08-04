from flask import Flask, render_template


app= Flask(__name__)

@app.route('/')
def route():
	return render_template('adventure.html')
@app.route('/left')
def projects():
	return render_template('left.html')

@app.route('/right')
def projects1():
	return render_template('right.html')

@app.route('/right/red')
def projects2():
	return render_template('rightred.html')

@app.route('/right/black')
def projects3():
	return render_template('rightblack.html')

app.run(debug=True)