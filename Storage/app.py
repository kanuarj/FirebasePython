import pyrebase

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        upload = request.files['upload']
        storage.child("images/new.mp4").put(upload)
        return redirect(url_for('uploads'))
    return render_template('index.html')


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        return redirect(url_for('basic'))
    if True:
        links = storage.child('images/new.mp4').get_url(None)
        return render_template('upload.html', l=links)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
