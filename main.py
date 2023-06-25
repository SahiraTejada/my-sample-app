from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healtcheck")
async def root():
    return {"status": {
        "acceptRequest": True,
        "DbConnectionStatus" : "Failing"
    }
}
