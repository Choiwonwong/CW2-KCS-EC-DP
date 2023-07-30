# # 오늘의 테이블
from fastapi import FastAPI
from routers import otas, webs
import uvicorn
from database.connection import Settings

app = FastAPI()

settings = Settings()

app.include_router(webs.router)
app.include_router(otas.router, prefix='/otas')

@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)