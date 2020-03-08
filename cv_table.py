import psycopg2 as psy


con = psy.connect   (   host="localhost",
                        database="flaskhtml",
                        user="postgres",
                        password="Diop1957+",
                        port="5432"
                        )



cur = con.cursor()
#cur.execute("drop table users_cv")

cur.execute("""CREATE TABLE  IF NOT EXISTS  users_cv(
                        id_user SERIAL PRIMARY KEY,
                        name VARCHAR(255) ,
                        email VARCHAR(255) ,
                        subject VARCHAR(255) ,
                        message VARCHAR(255))
        """)

print("yesssssssss!!!!!!")


con.commit()
con.close()
