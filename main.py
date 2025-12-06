from fastapi import FastAPI


app = FastAPI()


@app.get("/users")
async def read_user():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_user2():
    return ["Rick", "Morty"]
