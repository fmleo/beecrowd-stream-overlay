import uvicorn
from fastapi import FastAPI
from fastapi import WebSocket, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from asyncio import sleep

from utils import get_user_data_in_rank

from config import config

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/{institution}/{username}")
async def index(request: Request, institution: str, username: str):
    socket_url = f"ws://{config['host']}:{config['port']}/ws/{institution}/{username}"
    ctx = {"request": request, "socket_url": socket_url}
    return templates.TemplateResponse("index.html", ctx)


@app.websocket("/ws/{institution}/{username}")
async def get_data(websocket: WebSocket, institution: str, username: str):
    await websocket.accept()

    while True:
        data = await get_user_data_in_rank(institution)
        try:
            filtered_data = list(filter(lambda i: i.get("username") == username, data))[0]
            await websocket.send_json(filtered_data)
        except IndexError:
            await websocket.close(code=400, reason=f"User {username} not found in {institution}")

        await sleep(60)


if __name__ == '__main__':
    print("Adicione uma nova source de navegador no OBS com a seguinte url:")
    print(f"http://{config['host']}:{config['port']}/instituicao/nomeDeUsuario/")
    print("Por exemplo:")
    print(f"http://{config['host']}:{config['port']}/ifrs/fmleonardo/")

    uvicorn.run(app=app, **config)
