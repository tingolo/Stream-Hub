from fastapi import FastAPI
from application import Application


fastapiApp = FastAPI()

app = Application()
app.run(entryPoint = fastapiApp)