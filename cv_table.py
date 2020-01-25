import psycopg2 as psy


con = psy.connect   (   host="localhost",
                        database="flaskhtml",
                        user="postgres",
                        password="Diop1957+",
                        port="5432"
                        )



cur = con.cursor()
# cur.execute("drop table users_cv")

cur.execute("""CREATE TABLE  IF NOT EXISTS  users_cv(
                        id_user SERIAL PRIMARY KEY,
                        email VARCHAR(255) ,
                        message VARCHAR(255))
        """)




con.commit()
con.close()
