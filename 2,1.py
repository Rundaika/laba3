from fastapi import FastAPI

app = FastAPI()


@app.get("/qwerty/{item_id}")
async def read_item(item_id: int):
    return {item_id}
#http://127.0.0.1:8000/qwerty/rgokrejggkojkogeojgeior
#http://127.0.0.1:8000/qwerty/1235