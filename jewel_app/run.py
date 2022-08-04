import uvicorn
from logging import basicConfig

basicConfig(level="INFO", format="%(asctime)s %(message)s")

def main():
    uvicorn.run("jewel_app.main:app", host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()

