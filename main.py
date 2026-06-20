from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
import os

app = FastAPI()

# Базовая папка проекта
BASE_DIR = Path(__file__).resolve().parent

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Путь теперь ведет в папку templates
    html_path = BASE_DIR / "templates" / "index.html"
    
    if not html_path.exists():
        return HTMLResponse(content=f"<h1>Ошибка: Файл index.html не найден в {html_path}</h1>", status_code=404)
        
    content = html_path.read_text(encoding="utf-8")
    return HTMLResponse(content=content)

@app.get("/style.css")
async def get_css():
    css_path = BASE_DIR / "style.css"
    if css_path.exists():
        return FileResponse(css_path)
    return HTMLResponse(status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
