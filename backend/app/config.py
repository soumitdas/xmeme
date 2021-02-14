from os import getenv

ENVIRONMENT = getenv("ENVIRONMENT", "DEV")
MONGODB_URI = getenv("MONGODB_URI", "mongodb://localhost:27017")
HOST = getenv("HOST", "127.0.0.1")
PORT = int(getenv("PORT", "8081"))
BASE_URL = '{}:{}'.format(HOST, str(PORT))