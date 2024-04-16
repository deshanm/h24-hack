import json
from services.scraper_agent import WebsiteScraper
import utils.cache_me
from pydantic import BaseModel
from services.open_ai_agent import OpenaiUtils

class UseAiOptions(BaseModel):
    url: str
    type: str


class Scraper(BaseModel):
    url: str


cache = utils.cache_me.CacheMe(900)  # 15min


def get_site_content(website_url: str) -> str:
    content = cache.get(website_url)

    if content is None:
        web_scraper = WebsiteScraper(website_url)

        scrapedData = {
            "extract_meta_data": web_scraper.extract_meta_data(),
            "html": str(web_scraper.html.prettify()),
            "extract_assets": web_scraper.extract_assets(),
            "extract_links": web_scraper.extract_links(),
            "extract_headers": web_scraper.extract_headers(),
            "clean_html": web_scraper.clean_html,
        }
        cache.set(website_url, scrapedData)
        return scrapedData
    else:
        print("Site is cached-:" + website_url)
        return content


async def scrape_website(scraper: Scraper):
    return get_site_content(scraper.url)


async def use_ai(options: UseAiOptions):
    scrapedData = get_site_content(options.url)

    openAiUtils = OpenaiUtils()
    return openAiUtils.get_prompt_result(
        type=options.type,
        html=scrapedData["clean_html"],
        meta=scrapedData["extract_meta_data"],
    )
