from fastapi import FastAPI , Query;
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

app.add_middleware(CORSMiddleware,
                    allow_origins=["*"],
                    allow_credentials=False,
                    allow_methods=["*"],
                    allow_headers=["*"],
                    )
async def read_root():
    return {"Hello" : "World"}



@app.get("/order/apple")
async def read_fruit(color:str = Query(max_length=5)):
    if color == "red":
        ee = "🍎"
    else:
        ee = "🍏"
    return {"msg": ee+"がご注文されました"}

@app.get('/pineapple')
async def read_pineapple():
    return "🍍がご注文されました"

if __name__== "__main__":
    port = int(os.environ.get("PORT, 8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)


