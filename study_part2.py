'''
study_guide
part2

RJProctor

other files associated with this file
[Unit_3_Sprint_2_SQL_And_Databases_Study_Guide.md]
(C:\repos\Study-Guides\Unit_3_Sprint_2_SQL_And_Databases_Study_Guide.md)
[study_part1.py](C:\Repos\Study-Guides\study_part1.py)
'''

import sqlite3 
​
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()
​
# queries
# 1 Find the average invoice total for each customer, return the details for the first 5 ID's
invoice = cursor.execute('SELECT AVG(Total) FROM Invoice GROUP BY CustomerId LIMIT 5;').fetchall()

# 2 Return all columns in Customer for the first 5 customers residing in the United States
us_cust = cursor.execute('SELECT * FROM Customer WHERE Country = "USA" LIMIT 5;').fetchall()

# 3 Which employee does not report to anyone?
no_report = cursor.execute('SELECT EmployeeID, FirstName, LastName FROM Employee WHERE ReportsTo IS NULL;').fetchall()

# 4 Find the number of unique composers
composers = cursor.execute('SELECT COUNT (DISTINCT Composer) FROM Track LIMIT 10;').fetchall()

# 5 How many rows are in the Track table?
tracks = cursor.execute('SELECT COUNT(*) FROM Track;').fetchall()


​# queries with joins
# 6 Get the name of all Black Sabbath tracks and the albums they came off of
black_sabbath = cursor.execute('SELECT Track.Name, Album.Title, Track.Composer FROM Track INNER JOIN Album ON Track.AlbumId = Album.AlbumId WHERE Composer = "Black Sabbath";').fetchall()

# 7 What is the most popular genre by number of tracks?
genre_tracks = cursor.execute('SELECT COUNT(DISTINCT(Track.TrackId)), Genre.Name FROM Track INNER JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY COUNT(DISTINCT(Track.TrackId)) DESC LIMIT 1;').fetchall()

# 8 Find all customers that have spent over $45
cust_spend = cusror.execute('SELECT Customer.FirstName, Customer.LastName, Invoice.Total FROM Customer INNER JOIN Invoice ON CustomerID Customer.CustomerID = Invoice.CusomerID WHERE (Invoice.Total < 45);').fetchall()

# 9 Find the first and last name, title, and the number of customers each employee has helped. 
    # If the customer count is 0 for an employee, it doesn't need to be displayed. Order the 
    # employees from most to least customers.
cust_serv_count = cusror.execute('SELECT COUNT Customer.FirstName, Customer.LastName, Customer.Title,  FROM Customer OUTER JOIN Invoice  Invoice.SupportRepID = Employee.EmployeeID GROUP BY EmployeeID;').fetchall()

# 10 Return the first and last name of each employee and who they report to
to_report = cursor.execute('SELECT EmployeeID, FirstName, LastName, ReportsTo FROM Employee GROUP BY ReportsTo ORDER BY ReportsTo, LastName;').fetchall()


if __name__ == "__main__":
    print(cust_spend)
​
​
'''
Output 1: [(5.659999999999999,), (5.3742857142857146,), (5.659999999999999,), (5.659999999999999,), (5.802857142857143,)]
Output 2: [(16, 'Frank', 'Harris', 'Google Inc.', '1600 Amphitheatre Parkway', 'Mountain View', 'CA', 'USA', '94043-1351', '+1 (650) 253-0000', '+1 (650) 253-0000', 'fharris@google.com', 4), (17, 'Jack', 'Smith', 'Microsoft Corporation', '1 Microsoft Way', 'Redmond', 'WA', 'USA', '98052-8300', '+1 (425) 882-8080', '+1 (425) 882-8081', 'jacksmith@microsoft.com', 5), (18, 'Michelle', 'Brooks', None, '627 Broadway', 'New York', 'NY', 'USA', '10012-2612', '+1 (212) 221-3546', '+1 (212) 221-4679', 'michelleb@aol.com', 3), (19, 'Tim', 'Goyer', 'Apple Inc.', '1 Infinite Loop', 'Cupertino', 'CA', 'USA', '95014', '+1 (408) 996-1010', '+1 (408) 996-1011', 'tgoyer@apple.com', 3), (20, 'Dan', 'Miller', None, '541 Del Medio Avenue', 'Mountain View', 'CA', 'USA', '94040-111', '+1 (650) 644-3358', None, 'dmiller@comcast.com', 4)]
Output 3: [(1, 'Andrew', 'Adams')]
Output 4: [(852,)]
Output 5: [(3503,)]
Output 6: [('Sabbra Cadabra', 'Garage Inc. (Disc 1)', 'Black Sabbath')]
Output 7: [(1297, 'Rock')]
Output 8:
Output 9:
Output 10:
'''







