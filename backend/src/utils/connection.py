import sys

import psycopg2
from decouple import config

from src.utils.logger import logger

try:
    conn = psycopg2.connect(host=config('DB_HOST'), database=config('DB_NAME'), user=config('DB_USERNAME'), password=config('DB_PASSWORD'))
except psycopg2.DatabaseError as e:
    logger.error("ERROR: Unexpected error: Could not connect to RDS.")
    logger.error(e)
    sys.exit()