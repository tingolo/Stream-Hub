from fastapi import FastAPI
from application import Application


app = Application()
app.run(entryPoint = FastAPI())