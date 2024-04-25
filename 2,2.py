from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"Ну типа я да"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"ты зашел на айдишник рандомного чела": user_id}