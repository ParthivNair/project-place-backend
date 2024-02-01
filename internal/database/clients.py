from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from internal.database.postgres import Base


def get_postgres_client():
    """
    Test get client function
    :return:
    """
    # use app settings to create client
    client = None
    return client
