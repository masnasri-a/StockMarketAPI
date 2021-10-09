from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def test():
    return "test"

if __name__ == "__main__":
    uvicorn.run('main:app',port=8008)