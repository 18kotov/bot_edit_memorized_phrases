from settings import get_logger
from database_functions.commucation_with_db import post_query

logger = get_logger(__name__)

@post_query
def add_phrases(ask: str, answer: str):
    query = f"INSERT INTO memorized (ask, answer) VALUES('{ask}','{answer}');"
    return query









if __name__ == '__main__':
    pass

