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
        sql_update_query = """Update student_student set class_att_subj1 =class_att_subj1+1 where id=%s"""
        cursor.execute(sql_update_query, [id])
        sql_update_query = """Update student_student set subj1 = (class_att_subj1/%s)*100 where id=%s"""
        cursor.execute(sql_update_query, (classes_taken[0], id))
        connection.commit()        

    finally: 
        if (connection):
            cursor.close()
            connection.close()


def updatesubj2(id):
    classes_taken[1]+=1
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()
        sql_update_query = """Update student_student set class_att_subj2 = class_att_subj2+1 where id=%s"""
        cursor.execute(sql_update_query, [id])
        sql_update_query = """Update student_student set subj2 = (class_att_subj2/%s)*100 where id=%s"""
        cursor.execute(sql_update_query, (classes_taken[1], id))
        connection.commit()        

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def updatesubj3(id):
    classes_taken[2]+=1
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()
        sql_update_query = """Update student_student set class_att_subj3 = class_att_subj3+1 where id=%s"""
        cursor.execute(sql_update_query, [id])
        sql_update_query = """Update student_student set subj3 = (class_att_subj3/%s)*100 where id=%s"""
        cursor.execute(sql_update_query, (classes_taken[2], id))
        connection.commit()        

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()