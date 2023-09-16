from loguru import logger
from fastapi import FastAPI

app = FastAPI(
    title="LLAMA 2",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    pass
