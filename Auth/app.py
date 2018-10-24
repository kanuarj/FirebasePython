import pyrebase
from flask import *
app = Flask(__name__)
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'Please check your credentials'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('new.html', s=successful)
		except:
			return render_template('new.html', us=unsuccessful)

	return render_template('new.html')


if __name__ == '__main__':
	app.run()




























