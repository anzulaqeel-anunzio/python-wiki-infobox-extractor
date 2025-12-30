# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
from wiki_scraper.scraper import extract_infobox

def main():
    print("Starting Wikipedia Infobox Extractor...")
    
    data = extract_infobox()
    
    if data:
        print("\n--- Extracted Infobox Data ---")
        for k, v in list(data.items())[:5]: # Show first 5 for preview
            print(f"{k}: {v[:50]}..." if len(v) > 50 else f"{k}: {v}")
            
        with open("infobox_data.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("\nData saved to infobox_data.json")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
