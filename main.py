from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def read_root():
    return {"Hello": "World"} 

@app.get('/user')
async def read_user():
    return {"BACK"}

@app.get('/order/apple')
async def read_apple(color: str = Query(max_length=5)):
    if color == "red":
        ee = "🍎"
    else:
        ee = "🍏"

    #  ee = "🍎"  if  color == "red" else "🍏"
    return {"msg":ee+"が注文されました。"}

# @app.get('/order/apple/blue')
# async def read_apple():
#     ee = "🍏"
#     return {"msg",ee+"が注文されました。"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT",8000))
    uvicorn.run(app, host="0.0.0.0", port=port)