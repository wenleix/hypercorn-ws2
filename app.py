from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging

app = FastAPI()

logger = logging.Logger(__name__)

@app.websocket("/test")
async def test2(websocket: WebSocket):
    await websocket.accept()

    logger.error(f"Received: {await websocket.receive_text()}")
    try:
        await websocket.receive_text()
    except WebSocketDisconnect as e:
        logger.error(f"Client disconnected with code {e.code}")
        return

