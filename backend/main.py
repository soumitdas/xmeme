import uvicorn
from app.config import ENVIRONMENT, HOST, PORT

def main():
    uvicorn.run("app.main:app", host = HOST, port = PORT, reload = True)

if __name__ == "__main__":
    main()