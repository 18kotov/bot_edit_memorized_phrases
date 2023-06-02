from settings import get_logger
from database_functions.commucation_with_db import post_query


logger = get_logger(__name__)


@post_query
def delete_phrase(ask: str)->str:
    query = f"DELETE FROM memorized WHERE ask = '{ask}';"
    return query

