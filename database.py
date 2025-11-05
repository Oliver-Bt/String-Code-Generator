import sqlite3 as sql
import sys
import os
import Generation
def InitData():
    app = QApplication(sys.argv) 

    database = database()
    database.Create_database()
    exit()
    
    app.exec_()


class database:

    def Create_database(self):

        connexion = sql.connect("String-generation.db") #database created
        cursor = connexion.cursor()
        created= False
        #check if database exists
        try :
            cursor.execute("INSERT INTO String-generation (value, length, charset, source) VALUES (\"aB3xYz\" , \"6\" , \"alphanumeric\" , \"web-ui\")")
            cursor.execute("SELECT * FROM String-generation")
            print(cursor.fetchall())
            connexion.commit()
            #connexion.close()
            print("created")
            created = True
            
        except:
            created = False
            print("table not created or found")
            try:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS String-generation (
                    StringID INTEGER PRIMARY KEY , StringGenerated TEXT  
                );
                """)
                
                connexion.commit()
                #connexion.close()

            except:
                print("error")
        
    def execute_sql(self, sql):
        # Placeholder for SQL execution logic
        print(f"Executing SQL: {sql}")
