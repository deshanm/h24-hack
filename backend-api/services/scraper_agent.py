import copy
import requests
from bs4 import BeautifulSoup, NavigableString, Comment
from requests.exceptions import RequestException
from urllib.parse import urlsplit
from pydantic import BaseModel
import re

REQUEST_TIMEOUT = 7

class Link(BaseModel):
    link: str
    path: str


class Asset(BaseModel):
    asset: str
    url: str


class Header(BaseModel):
    header: str
    content: str


def remove_newlines_and_whitespace(text: str) -> str:
    cleaned_text = text.replace("\n", "").replace("\t", "")
    return cleaned_text

def is_only_whitespace(element):
    return (isinstance(element, NavigableString) and element.strip() == "") or (
        element.name == "div" and not element.get_text().strip()
    )

def normalize_whitespace(text: str) -> str:
    """
    Replace one or more whitespace characters (space, newline, tab, etc.)
    with a single space, and trim leading and trailing whitespace.
    """
    return re.sub(r'\s+', ' ', text).strip()

class WebsiteScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.html = self.fetch_html()
        self.clean_html = self.clean_html_content(copy.copy(self.html))

    def fetch_html(self):
        try:
            response = requests.get(self.url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            page_content = response.text
            return BeautifulSoup(page_content, "html.parser")
        except RequestException as err:
            raise Exception(str(err))

    def clean_html_content(self, html: BeautifulSoup) -> str:
        # Remove specific tags
        for tag_name in ["br", "script", "svg", "style", "iframe", "noscript", "footer", "header", "nav"]:
            for tag in html.find_all(tag_name):
                tag.decompose()

        footer_div_to_remove = html.find('div', {'data-corgi-component': 'footer-link-section'})
        if footer_div_to_remove:
            footer_div_to_remove.extract()

        header_div_to_remove = html.find('div', {'data-corgi-component': 'global-section-header-navigation'})
        if header_div_to_remove:
            header_div_to_remove.extract()

        # Remove all attributes except 'alt' for 'img' and 'href' for 'a'
        for tag in html.find_all(True):
             tag.attrs = {}

        # Truncate href attributes to 60 characters
        for a_tag in html.find_all('a', href=True):
            a_tag['href'] = a_tag['href'][:60]


        # Remove comments
        comments = html.findAll(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

        # Remove empty or whitespace-only tags
        for tag in html.find_all():
            if (not tag.contents or str(tag.get_text()).strip() == "") and tag.name != "br":
                tag.decompose()

      
        # Remove empty elements
        for element in html.find_all():
            if not element.get_text().strip():
                element.decompose()
    
        return html

    def get_url_path(self, url: str):
        parsed_url = urlsplit(url)
        return parsed_url.path

    def extract_meta_data(self) -> dict[str, str]:
        meta_data = {
            "title": "",
            "description": "",
            "keywords": "",
            "canonical": ""
        }
        
        # Extracting title tag
        title_tag = self.html.find("title")
        if title_tag:
            meta_data["title"] = normalize_whitespace(title_tag.get_text())

        # Extracting meta description and keywords
        for meta_tag in self.html.find_all("meta"):
            name = meta_tag.get("name")
            if name:
                name = name.lower()  # Normalize to lowercase
                if name in ["description", "keywords"]:
                    content = meta_tag.get("content")
                    if content:
                        meta_data[name] = normalize_whitespace(content)

        # Extracting canonical link
        canonical_link = self.html.find("link", rel="canonical")
        if canonical_link:
            meta_data["canonical"] = canonical_link.get("href")

        return meta_data

    def extract_assets(self) -> list[Asset]:
        page_assets: list[Asset] = list()

        assets_to_extract = ["img", "video"]

        assets = self.html.find_all(assets_to_extract)

        for asset in assets:
            if asset.has_attr("src"):
                data = Asset(asset=asset.name, url=asset["src"])
                page_assets.append(data)

        return page_assets

    def extract_links(self) -> list[Link]:
        links: list[Link] = list()

        for link in self.html.find_all("a"):
            # extract only in-site links
            if link.has_attr("href") and link["href"].startswith("/"):
                obj = Link(link=link.name, path=link["href"])
                if obj not in links:
                    links.append(obj)

        return links

    def extract_headers(self) -> list[Header]:
        page_headers: list[Header] = list()

        headers = self.html.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        for header in headers:
            data = Header(
                header=header.name, content=remove_newlines_and_whitespace(header.text)
            )
            page_headers.append(data)

        return page_headers

    def remove_comments(self, soup):
        # Remove all HTML comment elements
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

    def get_text(self):
        # Remove all HTML comment elements
        element = self.clean_html.find('body')
        #get_text with strip set to true
        text_content = element.get_text()

        return text_content
    