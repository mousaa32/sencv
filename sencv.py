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
    return  render_template('index.html')

@app.route('/contact',methods= ['GET','POST'])
def contact():
    if request.method == "POST":
        email=request.form['email'].lower().strip()
        message=request.form['message'].lower().strip()
        
        cur.execute("INSERT INTO users_cv(email,message) VALUES(%s,%s)",(email,message))
        con.commit()

        flash("mot de passe ou nom d'utilisateur incorect")
        # return redirect(url_for('index'))
    return  render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

                                           
