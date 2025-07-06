from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def serve_ui():
    """Opens the Home Page for State Job Heatmap"""
    with open("app/templates/index.html", "r") as file:
        return file.read()
