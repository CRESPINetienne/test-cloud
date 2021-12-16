from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "I have changed my text a second time"
