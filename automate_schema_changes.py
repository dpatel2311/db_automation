import pymysql
#from pymysql import connect
# Create the database connection directly
"""
connection = pymysql.connect(
    host='dbauto.mysql.database.azure.com',  
    user='rootdb',  
    password='Secret55',  
    database='dpatel',
)
"""
## Added this connection string to test ## 
## the python and sql on local database ##
connection = pymysql.connect(
    host='localhost',  
    user='custom',  
    password='custom123',  
    database='my_database',
)
# Path to the SQL file
script_path = 'update_projects_schema.sql'

# Read the SQL script from the file
with open(script_path, 'r') as file:
    sql_script = file.read()

# Create a cursor object to execute SQL queries
cursor = connection.cursor()  

# Execute each SQL statement individually (split by semicolon)
for statement in sql_script.split(';'):
    if statement.strip():  # Execute only non-empty statements
        cursor.execute(statement)

connection.commit()  # Commit all changes at once
cursor.close()  # Close the cursor
connection.close()  # Close the connection

print("Execution completed successfully")
