from dotenv import load_dotenv
import sqlalchemy as sa
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
        conn = sa.create_engine(
            f"mssql+pyodbc://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}?TrustServerCertificate={self.certificate}&driver=ODBC+Driver+18+for+SQL+Server"
        )

        if conn:
            print("Connection successful")
            return conn

        else:
            print("Connection failed")
