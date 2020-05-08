import psycopg2

classes_taken = [0, 0, 0]

def updatesubj1(id):
    classes_taken[0]+=1
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()
        sql_update_query = """Update student_student set subj1=(subj1_att+=1)/%s where id=%s"""
        cursor.execute(sql_update_query, (classes_taken[0], id))
        connection.commit()        

    finally: 
        if (connection):
            cursor.close()
            connection.close()


def updatesubj2(st_arr):
    classes_taken[1]+=1
    for i in range(9):
        if st_arr[i]==True :
            att_subj2[i]+=1

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()
        for i in range(9):
            attendence = (att_subj2[i]/classes_taken[1])*100
            sql_update_query = """Update student_student set subj2=%s where id=%s"""
            cursor.execute(sql_update_query, (attendence, i+1))
            connection.commit()        

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def updatesubj3(st_arr):
    classes_taken[2]+=1
    for i in range(9):
        if st_arr[i]==True :
            att_subj3[i]+=1

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()
        for i in range(9):
            attendence = (att_subj3[i]/classes_taken[2])*100
            sql_update_query = """Update student_student set subj3=%s where id=%s"""
            cursor.execute(sql_update_query, (attendence, i+1))
            connection.commit()        

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()