import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import markdownify 

# List of URLs to scrape
urls = [
    "https://www.home24.de/rabatt-angebote/",
    "https://www.home24.de/alle-geschenkgutscheine/",
    "https://www.home24.de/b2b/",
    "https://www.home24.de/nachhaltig/",
    "https://www.home24.de/ueber-uns/",
    "https://www.home24.de/gutscheine/",
    "https://www.home24.de/serviceversprechen/",
    "https://www.home24.de/deine-beratung/",
    "https://www.home24.de/ratgeber-federkernmatratzen-testsieger-stiftung-warentest/",
    "https://www.home24.de/ratgeber-welche-matratze-bei-rueckenproblemen/",
    "https://www.home24.de/ratgeber-welche-matratze-passt-zu-mir-test/",
    "https://www.home24.de/inspiration/",
    "https://www.home24.de/ratgeber-haertegrad/",
    "https://www.home24.de/ratgeber-was-kostet-eine-gute-matratze/",
    "https://www.home24.de/beratung-matratzen-guide/"
]

# Create a directory to store the markdown files if it doesn't exist
if not os.path.exists("markdown_files"):
    os.makedirs("markdown_files")

# Function to scrape and save content as markdown file
def scrape_and_save(url):
    # Get the page content using requests
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the page title
        title = soup.title.get_text().split("|")[0].strip()


        # Get the last part of the URL path
        url_path = urlparse(url).path
        filename = url_path.strip("/").split("/")[-1]

        # Save content to markdown file
        filepath = f"markdown_files/content_{filename}.md"
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"# {title}\n\n")
            file.write(markdownify.markdownify(str(soup), heading_style="ATX") )

        print(f"Scraped and saved content from: {url}")
    else:
        print(f"Failed to scrape content from: {url}")

# Loop through each URL and scrape content
for url in urls:
    scrape_and_save(url)
