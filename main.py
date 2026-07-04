from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from urllib.parse import quote

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
async def search_image(
    file: UploadFile = File(...),
    brand: str = Query(default=""),
    name: str = Query(default=""),
    tags: str = Query(default="")
):
    image_bytes = await file.read()

    # Suchbegriff aus KI-Ergebnissen zusammenbauen
    query_parts = [p for p in [brand, name, tags] if p]
    q = " ".join(query_parts) if query_parts else "fashion clothing"
    q_encoded = quote(q)

    shops = [
        {
            "name": "🛒 Zalando",
            "url": f"https://www.zalando.de/suche/?q={q_encoded}",
            "query": q
        },
        {
            "name": "👗 ASOS",
            "url": f"https://www.asos.com/search/?q={q_encoded}",
            "query": q
        },
        {
            "name": "♻️ Vinted",
            "url": f"https://www.vinted.de/catalog?search_text={q_encoded}",
            "query": q
        },
        {
            "name": "📦 Amazon",
            "url": f"https://www.amazon.de/s?k={q_encoded}",
            "query": q
        },
        {
            "name": "🏷️ eBay",
            "url": f"https://www.ebay.de/sch/i.html?_nkw={q_encoded}",
            "query": q
        },
        {
            "name": "💎 Farfetch",
            "url": f"https://www.farfetch.com/de/search/?q={q_encoded}",
            "query": q
        },
        {
            "name": "👟 StockX",
            "url": f"https://stockx.com/search?s={q_encoded}",
            "query": q
        },
        {
            "name": "📌 Pinterest",
            "url": f"https://www.pinterest.de/search/pins/?q={q_encoded}",
            "query": q
        },
        {
            "name": "🛍️ H&M",
            "url": f"https://www2.hm.com/de_de/search-results.html?q={q_encoded}",
            "query": q
        },
        {
            "name": "⚡ Shein",
            "url": f"https://www.shein.com/search?word={q_encoded}",
            "query": q
        },
        {
            "name": "🔍 Google Shopping",
            "url": f"https://www.google.com/search?tbm=shop&q={q_encoded}",
            "query": q
        },
        {
            "name": "🔎 Google Lens",
            "url": f"https://lens.google.com",
            "query": q
        },
    ]

    return {
        "query": q,
        "shops": shops,
        "total": len(shops)
    }
