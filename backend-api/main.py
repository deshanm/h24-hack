from services.scraper_agent import WebsiteScraper
import uvicorn
from controllers.api import UseAiOptions, Scraper, use_ai, scrape_website
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.open_ai_agent import OpenaiUtils

app = FastAPI()
openai_utils = OpenaiUtils()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/scrape")
async def post_scrape_website(options: Scraper):
    try:
        response = await scrape_website(options)
        return response
    except Exception as e:
        print(e)
        return str(e)


@app.post("/use_ai")
async def post_use_ai(options: UseAiOptions):
    try:
        response = await use_ai(options)
        return response
    except Exception as e:
        print(e)
        return str(e)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=7005,
        proxy_headers=True,
        workers=1,
        reload=True,
    )
