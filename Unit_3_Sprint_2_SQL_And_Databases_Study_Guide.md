'''
study_guide
part1

RJProctor

other files associated with this file
[study_part2.py](C:\Repos\Study-Guides\study_part2.py)
'''


# Unit 3 Sprint 2 SQL and Databases Study Guide
​
This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.
​
If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with [google](https://www.google.com) or [StackOverflow](https://www.stackoverflow.com). Only once you have exhausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.
​
Have fun studying!
​
## SQL
​
**Concepts:**
​
1. What is SQL?
---
SQL is used to communicate with a database. According to ANSI (American National Standards Institute), it is the standard language for relational database management systems. SQL statements are used to perform tasks such as update data on a database, or retrieve data from a database.

---
2. What is a RDBMS?
---
RDBMS stands for Relational Database Management System. RDBMS is the basis for SQL, and for all modern database systems such as MS SQL Server, IBM DB2, Oracle, MySQL, and Microsoft Access. The data in RDBMS is stored in database objects called tables.

---
3. What is an ETL pipeline?
---
ETL pipeline refers to a set of processes extracting data from one system, transforming it, and loading into some database or data-warehouse. ... It refers to any set of processing elements that move data from one system to another, possibly transforming the data along the way.

---
4. What is a schema?
---
A SQL database contains multiple objects such as tables, views, stored procedures, functions, indexes, triggers. We define SQL Schema as a logical collection of database objects. A user owns that owns the schema is known as schema owner. Database objects owner is a schema, and we define schema owners.

---
5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
---
In the context of transaction processing, the acronym ACID refers to the four key properties of a transaction: atomicity, consistency, isolation, and durability. Atomicity. All changes to data are performed as if they are a single operation.

	- Atomicity - a transaction to transfer funds from one account to another involves making a withdrawal operation from the first account and a deposit operation on the second. If the deposit operation failed, you don’t want the withdrawal operation to happen either.

    - Consistency - a database tracking a checking account may only allow unique check numbers to exist for each transaction

    - Isolation - a teller looking up a balance must be isolated from a concurrent transaction involving a withdrawal from the same account. Only when the withdrawal transaction commits successfully and the teller looks at the balance again will the new balance be reported.

    - Durability - A system crash or any other failure must not be allowed to lose the results of a transaction or the contents of the database. Durability is often achieved through separate transaction logs that can "re-create" all transactions from some picked point in time (like a backup).

---
6. Explain each of the table relationships and give an example for each
---
In a relational database, a relationship is formed by correlating rows belonging to different tables. A table relationship is established when a child table defines a Foreign Key column that references the Primary Key column of its parent table.

	- One-to-One - In a one-to-one relationship, one record in a table is associated with one and only one record in another table. For example, in a school database, each student has only one student ID, and each student ID is assigned to only one person.

	- One-to-Many - In a relational database, a one-to-many relationship exists when one row in table A may be linked with many rows in table B, but one row in table B is linked to only one row in table A. It is important to note that a one-to-many relationship is not a property of the data, but rather of the relationship itself.

	- Many-to-Many - A many-to-many relationship occurs when multiple records in a table are associated with multiple records in another table. ... Relational database systems usually don't allow you to implement a direct many-to-many relationship between two tables. Consider the example of keeping track of invoices.

    ---
​
## Syntax
For the following section, give a brief explanation of each of the SQL commands.
​---
1. **SELECT** - The SQL SELECT statement returns a result set of records, from one or more tables. A SELECT statement retrieves zero or more rows from one or more database tables or database views. In most applications, SELECT is the most commonly used data manipulation language (DML) command.

2. **WHERE** - The SQL WHERE clause is used to filter the results and apply conditions in a SELECT, INSERT, UPDATE, or DELETE statement.

3. **LIMIT** - The SQL LIMIT clause constrains the number of rows returned by a SELECT statement. For Microsoft databases like SQL Server or MSAccess, you can use the SELECT TOP statement to limit your results, which is Microsoft's proprietary equivalent to the SELECT LIMIT statement.

4. **ORDER** - The SQL ORDER BY clause is used to sort the data in ascending or descending order, based on one or more columns. Some databases sort the query results in an ascending order by default.

5. **JOIN** - A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

6. **CREATE TABLE** - The CREATE TABLE statement is used to create a table in a database. Tables are organized into rows and columns; and each table must have a name.

7. **INSERT** - The INSERT INTO statement of SQL is used to insert a new row in a table. There are two ways of using INSERT INTO statement for inserting rows: Only values: First method is to specify only the value of data to be inserted without the column names.

8. **DISTINCT** - SQL SELECT DISTINCT Statement - W3Schoolswww.w3schools.com › sql › sql_distinct. The SQL SELECT DISTINCT Statement The SELECT DISTINCT statement is used to return only distinct (different) values. Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

9. **GROUP BY** - The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country". The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

10. **ORDER BY** - The ORDER BY keyword is used to sort the result-set in ascending or descending order. The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.

11. **AVG** - SQL Server AVG() function is an aggregate function that returns the average value of a group. ... DISTINCT instructs the AVG() function to operate only on unique values. expression is a valid expression that returns a numeric value.

12. **MAX** - The SQL MAX function is used to return the maximum value of an expression in a SELECT statement.

13. **AS** - SQL AS keyword is used to give an alias to table or column names in the queries. In this way, we can increase the readability and understandability of the query and column headings in the result set.

---
​
## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
    ```
    student - string
    studied - string
    grade - int
    age - int
    sex - string
    ```
​
3. Fill the table with the following data
​
    ```
    'Lion-O', 'True', 85, 24, 'Male'
    'Cheetara', 'True', 95, 22, 'Female'
    'Mumm-Ra', 'False', 65, 153, 'Male'
    'Snarf', 'False', 70, 15, 'Male'
    'Panthro', 'True', 80, 30, 'Male'
    ```
​
4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
​
5. Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
​
    ```
    What is the average age? Expected Result - 48.8
    What are the name of the female students? Expected Result - 'Cheetara'
    How many students studied? Expected Results - 3
    Return all students and all columns, sorted by student names in alphabetical order.
    ```
​
## Query All the Tables!
​
### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.
​
### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?
​
**Joins**
​
6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to
​
## NoSQL
​
### Questions of Understanding
​
1. What is a document store?
​
2. What is a `key:value` pair? What data type in Python uses `key:value` pairs?
​
3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database
​
4. What are some of the trade-offs between SQL and NoSQL?
​
5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
    - B
    - A
    - S
    - E
