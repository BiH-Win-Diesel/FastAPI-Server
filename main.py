from fastapi import FastAPI,WebSocketDisconnect
from fastapi import WebSocket

from app import convert_audio_segment
app = FastAPI()


@app.websocket("/ws_a")
async def websocket_a(websocket: WebSocket):
    await websocket.accept()
    try: 
        while True:
            data = await websocket.receive_bytes()
            convert_audio_segment(data)
    except WebSocketDisconnect:
        print("Disconnected.....")

