"""
        Script made by: Emmanuel Amador Maldonado
        
        This script helps to make a connection to any postgres database
        This creates the engine using sqlachemy and psycopg2, this last
        library does not need to be installed as is a package inside
        sqlalchemy
        
        This script contains three functions
        
        - create_connection(database_name, host, user, password, port)
        
        - read_sql(path_to_sql_file, connection)
        
        - run_query(query, connection)
        
    
    
"""

import pandas as pd
from sqlalchemy import create_engine


class database(object):

    def __init__(self):
        
        dialect = "postgres"
        database_driver = "psycopg2"
        connection = None
          

    def connect(self, database_name:str, host:str, password:str, user:str, port:int | str, database_driver:str = ''):
        
        if database_driver != '':
            database_driver = "+"+database_driver
            self.database_driver = database_driver
        
        
        try:
            connect_string = f"postgresql{database_driver}://{user}:{password}@{host}:{str(port)}/{database_name}"
            conn = create_engine(connect_string)
            self.connection = conn
        except:
            print("Connection failed, check your parameters and try again")
        
        print("Connection Successful!")
        
        return




    def run_sql_file(file_name:str, self.connection):
        
        if self.connection == None:
            print("""The connection to the database you're trying to access has not been configured.
                
                    Run the function connect(**kargs), and try again
                """)
            
            return None
    
    
        try:
            with open(file_name, "r") as sql_file:
                sql_query = sql_file.read()
    
        except:
            print("File not found, check your file name")
            return None
        
        return pd.read_sql(sql_query, self.connection)
        
    def run_query(query:str, self.connection):
        
        if self.connection == None:
            print("""The connection to the database you're trying to access has not been configured.
                
                    Run the function connect(**kargs), and try again
                """)
            
            return None
        
        return pd.read_sql(query, self.connection)
        
        
def main():
    pass
    



if __name__ == "__main__":
    main()
        
            
    
