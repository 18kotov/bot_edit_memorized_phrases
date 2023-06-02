from settings import get_logger
from database_functions.commucation_with_db import get_data, get_value

logger = get_logger(__name__)

@get_value
@get_data
def get_quantity_phrases_add_today() -> str:
    quite = "SELECT COUNT(*) AS row_count FROM memorized WHERE date = CURRENT_DATE;"
    return quite



if __name__ == '__main__':
    pass
