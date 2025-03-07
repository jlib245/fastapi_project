from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello world!"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

