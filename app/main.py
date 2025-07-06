from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from routes import fetch_data, ui

app = FastAPI()

app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")
app.mount("/templates", StaticFiles(directory="app/templates"), name="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fetch_data.router)
app.include_router(ui.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)