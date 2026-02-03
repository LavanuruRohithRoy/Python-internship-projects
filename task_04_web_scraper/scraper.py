import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    
    #Fetch HTML content from the given URL

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")
        return None


def parse_headlines(html):

    #Extract news headlines from HTML
    
    soup = BeautifulSoup(html, "html.parser")

    headlines = []
    rows = soup.find_all("span", class_="titleline")

    for row in rows:
        anchor = row.find("a")
        if anchor:
            headlines.append(anchor.get_text(strip=True))

    return headlines


def display_headlines(headlines):
    
    #Display extracted headlines neatly
    
    if not headlines:
        print("No headlines found")
        return

    print("\n📰 Latest News Headlines:\n")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")


def main():
    url = "https://news.ycombinator.com/"
    html = fetch_page(url)

    if html:
        headlines = parse_headlines(html)
        display_headlines(headlines)


if __name__ == "__main__":
    main()

