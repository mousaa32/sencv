from flask import Flask,render_template,request,redirect,url_for,flash,session,escape
import psycopg2 as psy

def connexiondb():
        try:
            con = psy.connect(
                    host="localhost",
                    database="flaskhtml",
                    user="postgres",
                    password="Diop1957+",
                    port=5432
                    )
            return con
        except(Exception) as error:
            print("probleme connection",error)

con = connexiondb()
cur = con.cursor()

app = Flask(__name__)
app.secret_key="flash message"
#connect to the database

@app.route('/')
def index():
    cur.execute("select * from users_cv")
    liste_mail=cur.fetchall()
    con.commit()
    for i in liste_mail:
        print(i)

    return  render_template('index.html')



"""@app.route('/contact',methods= ['GET','POST'])
def contact():
        
    cur.execute("select email from users_cv")
    liste_mail=cur.fetchall()
    con.commit()

    if request.method == "POST":
        name=request.form['name'].lower().strip()
        email=request.form['email'].lower().strip()
        subject=request.form['subject'].lower().strip()
        message=request.form['message'].lower().strip()
        ####pour verifier  si le nom existe deja
        control_ref=False
        for row in liste_mail:
            if row[0] == email:
                control_ref =True
                break
        if control_ref == True  :
            flash("le mail exist deja")

        else:
            cur.execute("INSERT INTO users_cv(name,email,subject,message) VALUES(%s,%s,%s,%s)",(name,email,subject,message))
            con.commit()
            flash("message envoyé avec avec succé")
    return redirect(url_for('index'))"""

@app.route('/contact',methods= ['GET','POST'])
def contact():
    if request.method == "POST":
        name=request.form['name'].lower().strip()
        email=request.form['email'].lower().strip()
        subject=request.form['subject'].lower().strip()
        message=request.form['message'].lower().strip()
        
        cur.execute("INSERT INTO users_cv(name,email,subject,message) VALUES(%s,%s,%s,%s)",(name,email,subject,message))
        con.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

                                           
