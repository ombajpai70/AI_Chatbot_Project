import oracledb
import oracledb

oracledb.init_oracle_client(
    lib_dir=r"D:\oracle\instantclient_23_0"
)
from config import (
    DB_HOST,
    DB_PORT,
    DB_SERVICE,
    DB_USER,
    DB_PASSWORD
)


def get_connection():

    dsn = oracledb.makedsn(
        DB_HOST,
        DB_PORT,
        service_name=DB_SERVICE
    )

    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=dsn
    )

    return connection