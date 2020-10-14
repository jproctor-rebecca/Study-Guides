'''
study_guide
part2

RJProctor

other files associated with this file
[Unit_3_Sprint_2_SQL_And_Databases_Study_Guide.md]
(C:\repos\Study-Guides\Unit_3_Sprint_2_SQL_And_Databases_Study_Guide.md)
[study_part2.py](C:\Repos\Study-Guides\study_part2.py)
'''
import sqlite3



# 2 Create a table with the following columns
# create statement
def create_table(conn):  
    curs = conn.cursor()  
    create_statement = '''
    CREATE TABLE IF NOT EXISTS students (
        student char(40),
        studied char(40),
        grade INTEGER,
        age INTEGER,
        sex char(15)
    );
    '''
    curs.execute(create_statement)
    conn.commit()

# 3 Fill the table with the following data
# insert statement
def insert_data(conn):
    curs = conn.cursor()
    student_data = [
        ('Lion-O', 'True', 85, 24, 'Male'),
        ('Cheetara', 'True', 95, 22, 'Female'),
        ('Mumm-Ra', 'False', 65, 153, 'Male'),
        ('Snarf', 'False', 70, 15, 'Male'),
        ('Panthro', 'True', 80, 30, 'Male'),
    ]

    for row in student_data:
        insert_statement = ''' 
        INSERT INTO students
        (student, studied, grade, age, sex)
        VALUES(?,?,?,?,?); '''
        curs.execute(insert_statement, row)

    conn.commit()
    

# 4 Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
​#curs.close()


if __name__ = '__main__':
    conn = sqlite3.connect('study_part3.sqlite')
    create_table(conn)
    insert_data(conn)
    conn.close()

# # 5 Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
# ​
#     ```
#     What is the average age? Expected Result - 48.8



#     What are the name of the female students? Expected Result - 'Cheetara'



#     How many students studied? Expected Results - 3



#     Return all students and all columns, sorted by student names in alphabetical order.




#     ```
