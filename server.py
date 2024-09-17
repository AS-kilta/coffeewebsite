from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from decouple import config

from getPic import getImage

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/mnt", StaticFiles(directory="static"), name="static")

coffeeThoughtsPath = config("THOUGHTS_PATH")

@app.get("/")
async def root(request: Request):
	getImage()
	thoughts = []
	with open(coffeeThoughtsPath, "r") as ff:
		thoughts = [thing for thing in ff.read().split("\n")[::-1] if thing != ""]
	print(thoughts)
	return templates.TemplateResponse("index.html", {"request": request, "thoughts": thoughts})
