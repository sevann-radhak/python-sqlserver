import pyodbc
import PersonModel

server = '<your_server>.database.windows.net'
db = '<your_database>'
user = '<your_username>'
password = '<your_password>'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+ password)
conn.autocommit = True 
                        
def delete_persons(id: int):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM test_db.dbo.persons WHERE ID = ?"
        
        cursor.execute(query, (id))
        
        return cursor.rowcount
    except Exception as e:
            print("Error: " + str(e))


def get_persons():
    try:
        cursor = conn.cursor()    
        get_persons = 'SELECT * FROM test_db.dbo.persons'    
        cursor.execute(get_persons)
        
        for row in cursor:
            print(row)
        
        return cursor
    except Exception as e:
        print("Error: " + str(e))


def insert_persons(person: PersonModel.PersonModel):
    try:
        if person is None:
            raise Exception("Person is null")
        
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO test_db.dbo.persons (LastName, FirstName, Address, City) VALUES (?, ?, ?, ?)", (person.LastName, person.FirstName, person.Address, person.City))
        
        return cursor.rowcount
    except Exception as e:
        print("Error: " + str(e))


def update_persons(person: PersonModel.PersonModel):
    try:
        if person is None:
            raise Exception("Person is null")
        
        cursor = conn.cursor()
        query = "UPDATE test_db.dbo.persons SET LastName = ?, FirstName = ?, Address = ?, City = ? WHERE ID = ?"
        
        cursor.execute(query, (person.LastName, person.FirstName, person.Address, person.City, person.Id))
        
        return cursor.rowcount
    except Exception as e:
            print("Error: " + str(e))

print("Connection successful.")