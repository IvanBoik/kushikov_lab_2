from typing import Any, Dict

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import logging

from process import process, u_list

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="static/templates")

FAKS_COUNT = 4
EQUATIONS_COUNT = 55

logger = logging.getLogger("uvicorn.error")


@app.get("/initial_equations")
async def get_initial_equations():
    return u_list


# Точка входа в приложение
@app.get("/")
async def main(
        request: Request,
        initial_equations=Depends(get_initial_equations)
):
    return templates.TemplateResponse(name="index.html", context={
        "request": request,
        "initial_equations": initial_equations
    })


# Метод обработки введенных пользователем значений. Возвращает статус в виде строки. Если статус = "Выполнено",
# то на других страницах будут отображаться нарисованные графики. Пока этот метод не вызван, графики отображаться не должны
@app.post("/draw_graphics")
async def draw_graphics(body: Dict[Any, Any]):
    try:
        process(body["initial_equations"], body["faks"], body["equations"], body["restrictions"])
        return {"status": "Выполнено"}
    except Exception:
        return {"status": "Ошибка"}


@app.get("/graphic")
async def get_graphic(request: Request):
    return templates.TemplateResponse(name="graphic.html", context={
        "request": request
    })


@app.get("/diagrams")
async def get_diagrams(request: Request):
    return templates.TemplateResponse(name="diagrams.html", context={
        "request": request
    })


@app.get("/faks")
async def get_faks(request: Request):
    return templates.TemplateResponse(name="faks.html", context={
        "request": request
    })
