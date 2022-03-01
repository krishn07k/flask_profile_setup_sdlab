from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_pg():
    return render_template('home.html')

@app.route('/prof',methods=['POST', 'GET'] )
def setup_pro():
    if request.method == 'GET':
        return render_template('setup_profile.html')
    else:
        data_recv=(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['gender'],
            request.form['dob'],
            
        )

        temp='INSERT INTO profile (Name, Email, Phone, Gender, Dob) VALUES(?,?,?,?,?)'

        connie=sqlite3.connect('profile.db')

        c=connie.cursor()

        c.execute(temp,data_recv)
        
        connie.commit()
        connie.close()
        return render_template('success.html')





if __name__ == '__main__':
    app.run()