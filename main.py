# # 오늘의 테이블
from fastapi import FastAPI
from routers import otas, webs
import uvicorn

app = FastAPI()

app.include_router(webs.router)
app.include_router(otas.router, prefix='/otas')

if __name__=="__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)