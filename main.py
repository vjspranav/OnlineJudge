from fastapi import FastAPI, Request
from languages.languagehandler import get_language_handler

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/execute")
async def language_handler(request: Request):
    request_json = await request.json()
    language = request_json["language"]
    input_files = request_json["input_files"]
    output_files = request_json["output_files"]
    user_input = request_json["user_input"]

    handler = get_language_handler(language, input_files, output_files, user_input)

    handler.execute()
    return {"message": "Executed"}