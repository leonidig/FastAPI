from .. import app


@app.get("/")
async def dafault():
    return {"hello": "world"}