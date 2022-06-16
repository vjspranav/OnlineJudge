from fastapi import FastAPI, Request, Body
from languages.languagehandler import PythonHandler, CHandler, CppHandler

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

    if language == "python":
        handler = PythonHandler(language, input_files, output_files, user_input)
    elif language == "c":
        handler = CHandler(language, input_files, output_files, user_input)

    handler.execute()
    return {"message": "Executed"}