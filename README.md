# Product Price Scraper

Python tool that scrapes product data (title, price, rating, stock status, URL)
from a paginated catalogue and exports it to CSV, JSON and Excel.

## Features
- Automatic pagination
- Retry with backoff on network errors
- Polite delay between requests
- Clean, structured output (UTF-8, Excel-friendly)
- Easy to adapt: only the CSS selectors in parse_product() change per site

## Install & run
pip install -r requirements.txt
python scraper.py --max-pages 5 --out books

## Options
--url        Start page (default: demo site)
--max-pages  Pages to scrape (default: 3)
--delay      Seconds between requests (default: 1.0)
--out        Output file name without extension (default: products)

## Need a custom scraper for your website?
I build web scrapers, scheduled data collection and automation scripts in Python.
Telegram: @factorbaz
