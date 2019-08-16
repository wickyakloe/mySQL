import os
import datetime
import pymysql

# Get username from Cloud 9 workspace
# (modify this variable if running on another environment)
username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(host='localhost',
                              user=username,
                              password='',
                              db='Chinook')
                              
try:
    #Run a query
    # with connection.cursor() as cursor:
    #     sql ="SELECT * FROM Artist;"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print(result)
    # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #     sql ="SELECT * FROM Genre;"
    #     cursor.execute(sql)
    #     for row in cursor:
    #         print(row)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS Friends(name char(20), age int, DOB datetime);")
finally:
    # Close the connection, regardless of whether the above was succesful
    connection.close()
    
# Create table    
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                           Friends(name char(20), age int, DOB datetime);""")
#         # Note that the above will still display a warning (not error) if the
#         # table already exists
# finally:
#     connection.close()

# Insert many
# try:
#     with connection.cursor() as cursor:
#         rows = [("bob", 21, "1990-02-06 23:04:56"),
#                 ("jim", 56, "1955-05-09 13:12:45"),
#                 ("fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
#         connection.commit()
# finally:
#     connection.close()

# Update
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
#         connection.commit()
# finally:
#     connection.close()

# Alternate update
# try:
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
#                       (23, 'bob'))
#         connection.commit()
# finally:
#     connection.close()

# Update many
# try:
#     with connection.cursor() as cursor:
#         rows = [(23, 'bob'),
#                 (24, 'jim'),
#                 (25, 'fred')]
#         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
#                           rows)
#         connection.commit()
# finally:
#     connection.close()

# Delete
# try:
#     with connection.cursor() as cursor:
#         rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
#         connection.commit()
# finally:
#     connection.close()

# Alternate delete
# try:
#     with connection.cursor() as cursor:
#         rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
#         connection.commit()
# finally:
#     connection.close()

# Delete many
# try:
#     with connection.cursor() as cursor:
#         rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'jim'])
#         connection.commit()
# finally:
#     connection.close()

# Delete Where In
# try:
#     with connection.cursor() as cursor:
#         list_of_names = ['fred', 'Fred']
#         # Prepare a string with same number of placeholders as in list_of_names
#         format_strings = ','.join(['%s'] * len(list_of_names))
#         cursor.execute(
#             "DELETE FROM Friends WHERE name in ({});".format(format_strings),
#             list_of_names)

#         connection.commit()
# finally:
#     connection.close()