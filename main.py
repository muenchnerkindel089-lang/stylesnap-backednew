from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "StyleSnap Backend läuft!"}

@app.post("/search")
async def search_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    q = "fashion clothing"
    shops = [
        {"name": "Zalando", "url": f"https://www.zalando.de/suche/?q={q}"},
        {"name": "ASOS", "url": f"https://www.asos.com/search/?q={q}"},
        {"name": "Vinted", "url": f"https://www.vinted.de/catalog?search_text={q}"},
    ]
    return {"shops": shops, "query": q}
