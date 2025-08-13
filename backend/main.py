from fastapi import FastAPI
from core.config import settings

app=FastAPI(title=settings.PROJECT_NAME,version=settings.ROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"msg":"Hello Fastapi"}