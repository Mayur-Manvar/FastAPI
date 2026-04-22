from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql+pyodbc://local-admin:admin-local@(localdb)\\MSSQLLocalDB/FastApiDemo?driver=ODBC+Driver+17+for+SQL+Server")
#engine = create_engine("mssql+pyodbc://@localhost/FastApiDemo?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes")
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
