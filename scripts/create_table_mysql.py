import mysql.connector

db_conn = mysql.connector.connect(host="localhost", port="30306", user="root", 
password="2705895a", database="acit3495")

db_cursor = db_conn.cursor()

db_cursor.execute('''
          CREATE TABLE IF NOT EXISTS student_grades
          (id INT NOT NULL AUTO_INCREMENT, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(100) NOT NULL,
           course_name VARCHAR(50) NOT NULL,
           grade INT NOT NULL,
           CONSTRAINT student_grades_pk PRIMARY KEY (id))
          ''')
db_conn.commit()
db_conn.close()
