# Wikipedia Infobox Extractor (Python)

A Python script to extract structured data from Wikipedia Infoboxes (e.g., for companies, countries, people).

> [!NOTE]
> This tool parses the HTML of Wikipedia pages. For large-scale data extraction, DBpedia or the official MediaWiki API is recommended.

## Features

-   **Targeted Extraction**: specifically looks for the `table.infobox`.
-   **Key-Value Parsing**: Converts table rows into a dictionary.
-   **JSON Export**: Saves the extracted data to a JSON file.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python run_extractor.py
```

## Configuration

Edit `wiki_scraper/config.py` to change the target Wikipedia URL.

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
