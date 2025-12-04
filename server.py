from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from decouple import config

from getPic import getImage
from getAIQuote import ai_quote

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

coffeeThoughtsPath = config("THOUGHTS_PATH")

@app.head("/")
async def head_root():
    return {"status": "ok"}

@app.get("/")
async def root(request: Request):
	getImage()
	thoughts = []
	aiResponse = await ai_quote()
	with open(coffeeThoughtsPath, "r") as ff:
		thoughts = [thing for thing in ff.read().split("\n")[::-1] if thing != ""]
	return templates.TemplateResponse("index.html", {"request": request, "thoughts": thoughts, "aiResponse": aiResponse})
