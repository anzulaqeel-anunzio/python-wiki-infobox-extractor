# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests
from bs4 import BeautifulSoup
from .config import WIKI_URL, USER_AGENT

def extract_infobox():
    headers = {"User-Agent": USER_AGENT}
    print(f"Fetching {WIKI_URL}...")

    try:
        response = requests.get(WIKI_URL, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching page: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, "html.parser")
        infobox = soup.select_one("table.infobox")

        if not infobox:
            print("No infobox found on this page.")
            return None

        data = {}
        rows = infobox.find_all("tr")

        for row in rows:
            header = row.find("th")
            value = row.find("td")

            if header and value:
                key = header.get_text(strip=True)
                val = value.get_text(separator=" ", strip=True) # Join multiple elements with space
                data[key] = val
        
        return data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
