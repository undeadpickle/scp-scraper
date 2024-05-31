import requests
from bs4 import BeautifulSoup


def scrape_scp_website(url):
    """Scrape the given SCP website and return the extracted SCP entries with titles."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all SCP article titles and numbers
    scp_entries = []
    for li in soup.select("ul li"):
        text = li.get_text(strip=True)
        if text.startswith("SCP-"):
            scp_entries.append(text)

    return scp_entries


if __name__ == "__main__":
    url = "http://scp-wiki.wikidot.com/scp-series"
    data = scrape_scp_website(url)
    print("SCP Articles found on the website:")
    for entry in data:
        print(entry)
