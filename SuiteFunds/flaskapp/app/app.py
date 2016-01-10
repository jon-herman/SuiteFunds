from flask import Flask, render_template, request
import SuiteFunds

app = Flask(__name__)

# Home page
@app.route("/")
def loadPage():
	print("loaded")
	return render_template('index.html')

# On form submission
@app.route("/submit", methods=['GET', 'POST'])
def getPayments():
	if request.method == 'POST':
		input = request.form['input']
		funds = SuiteFunds.getFunds(input)
		payments = []
		threshold = 5
		payments = SuiteFunds.getPayments(funds, payments, threshold)
		# payments = SuiteFunds.main()
		return render_template('index.html', payments  = payments)
	
	else:
		loadPage()

	

if __name__ == "__main__":
    app.run(debug=True)

