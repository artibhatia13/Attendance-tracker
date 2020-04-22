import psycopg2

def updatesubj1(stname):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres123",
            host="localhost",
            port="5432",
            database="studentdb")

        cursor = connection.cursor()

        # Update single record
        sql_update_query = """Update student_student set subj1= 1 where name=stname"""
        cursor.execute(sql_update_query, (subj, id))
        connection.commit()        

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()