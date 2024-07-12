import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()


class Connection:
    def __init__(self):
        self.driver = os.getenv("DB_DRIVER")
        self.server = os.getenv("DB_SERVER")
        self.port = os.getenv("DB_PORT")
        self.db = os.getenv("DB_NAME")
        self.uid = os.getenv("DB_UID")
        self.pwd = os.getenv("DB_PWD")
        self.certificate = os.getenv("DB_CERTIFICATE")

    @property
    def connection(self):
        conn = pyodbc.connect(
            f"Driver={self.driver};"
            f"Server={self.server},{self.port};"
            f"Database={self.db};"
            f"TrustServerCertificate={self.certificate};"
            f"UID={self.uid};"
            f"PWD={self.pwd};"
        )
        if conn:
            print("Connection successful")
            return conn

        else:
            print("Connection failed")
