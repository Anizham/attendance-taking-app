from flask import Flask, request, render_template
import pyrebase 
import datetime

#Add Config APIs

config = {
    "apiKey": "AIzaSyAZ0kvRLLJNFj2nv_PZPKY3siIJlYjPrzA",
    "authDomain": "attendance-taking-app.firebaseapp.com",
    "databaseURL": "https://attendance-taking-app.firebaseio.com",
    "storageBucket": "attendance-taking-app.appspot.com",
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

app = Flask(__name__,)





@app.route('/',methods=['POST','GET'])   
def index1():

    submit = False
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            x = datetime.datetime.now()
            x = x.strftime("%Y-%m-%d %H:%M:%S")

            name = request.form.get('name')
            email = request.form.get('email')
            number = request.form.get('number')
            regno = request.form.get('regno')

            print(name,email,number,regno)


            payload = {'time': x, 'name' : name,'email': email,'number':number, "regno" : regno}

            db.child('teachbotattendence').push(payload)


            return render_template('index.html', submit=True, name = payload['name'])





    return render_template('index.html', submit = False)

@app.route('/team',methods=['POST','GET'])   
def team():
    return render_template('team.html')


if __name__ =='__main__':  
    app.run(host='0.0.0.0',debug=True
    ) 